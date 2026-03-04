import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error # <-- NEW IMPORT

# --- 1. MENTAL CONFIGURATION ---
KEYS = ["store_id", "sku"]
CATS = ["store_id", "sku", "dow", "month"]

def make_features(df):
    """Mathematical Block: Dates, Lags, and Rolling Means"""
    df = df.sort_values(KEYS + ["date"]).reset_index(drop=True)
    
    df["dow"] = df["date"].dt.dayofweek.astype("int8")
    df["month"] = df["date"].dt.month.astype("int8")
    
    grp = df.groupby(KEYS)["sales"]
    
    for lag in [1, 7, 14, 28]:
        df[f"lag_{lag}"] = grp.shift(lag)
    
    grp_shift = df.assign(tmp=grp.shift(1)).groupby(KEYS)["tmp"]
    for w in [7, 14, 28]:
        df[f"roll_mean_{w}"] = grp_shift.transform(lambda x: x.rolling(w, min_periods=1).mean())
        
    return df

def main():
    # --- 2. READ AND NORMALIZE DATA ---
    df = pd.read_csv("data/train.csv")
    df = df.rename(columns={
        "family": "sku",          
        "store_nbr": "store_id", 
        "onpromotion": "promo",  
    })
    df["date"] = pd.to_datetime(df["date"])

    # --- 3. THE PANEL (Fill time gaps) ---
    dates = pd.date_range(df["date"].min(), df["date"].max())
    idx = pd.MultiIndex.from_product(
        [df["sku"].unique(), df["store_id"].unique(), dates], 
        names=["sku", "store_id", "date"]
    )
    df = df.set_index(["sku", "store_id", "date"]).reindex(idx).reset_index()

    # --- 4. IMPUTATION (Retail Rule: No record = Zero sales) ---
    df["sales"] = df["sales"].fillna(0.0) 
    if "promo" in df.columns: 
        df["promo"] = df["promo"].fillna(0)
    
    df = make_features(df)
    df = df.dropna(subset=["lag_28"]).copy()
    
    for c in CATS:
        df[c] = df[c].astype("category")

    # --- 5. TRAINING (XGBoost) ---
    features = [c for c in df.columns if c not in ["sales", "date", "id"]]
    
    cutoff = df["date"].max() - pd.Timedelta(days=28)
    train = df[df["date"] <= cutoff]
    valid = df[df["date"] > cutoff]

    model = xgb.XGBRegressor(
        n_estimators=1000, 
        objective="count:poisson", 
        random_state=42,
        enable_categorical=True,   
        tree_method="hist"         
    )
    
    model.fit(
        train[features], train["sales"], 
        eval_set=[(valid[features], valid["sales"])], 
        early_stopping_rounds=50,
        verbose=False
    )

    # --- 5.5 EVALUATION METRICS (Measuring the Validation Set) ---
    print("\n--- Model Evaluation (Last 28 Days) ---")
    y_true = valid["sales"]
    y_pred = np.maximum(model.predict(valid[features]), 0)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    # WAPE avoids division by zero when actual sales are 0
    wape = np.sum(np.abs(y_true - y_pred)) / np.sum(y_true)

    print(f"RMSE: {rmse:.4f}")
    print(f"MAE:  {mae:.4f}")
    print(f"WAPE: {wape:.2%}\n")

    # --- 6. RECURSIVE FORECAST (100 days into the future) ---
    work = df.copy()
    
    if "promo" in work.columns:
        static = work.groupby(KEYS)[["promo"]].last().reset_index()
    else:
        static = work[KEYS].drop_duplicates()
        
    preds = []

    for d in pd.date_range(work["date"].max() + pd.Timedelta(days=1), periods=100):
        hist = work[work["date"] >= d - pd.Timedelta(days=60)].copy()
        
        today = static.copy()
        today["date"] = d
        today["sales"] = np.nan
        
        tmp = make_features(pd.concat([hist, today], ignore_index=True))
        day_df = tmp[tmp["date"] == d].copy()
        
        for c in CATS: 
            day_df[c] = day_df[c].astype(df[c].dtype)
        
        y_hat = np.maximum(model.predict(day_df[features]), 0)
        
        today["sales"] = y_hat
        work = pd.concat([work, today], ignore_index=True)
        
        day_df["y_pred"] = y_hat
        preds.append(day_df)

    # --- 7. EXPORT ---
    final_df = pd.concat(preds, ignore_index=True)[KEYS + ["date", "y_pred"]]
    final_df.to_csv("forecast_100d_xgb.csv", index=False)
    print("Forecast complete. Results saved successfully.")

if __name__ == "__main__":
    main()
