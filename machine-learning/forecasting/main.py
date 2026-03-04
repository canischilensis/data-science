import pandas as pd
import numpy as np
import lightgbm as lgb

# --- 1. CONFIGURACIÓN MENTAL ---
KEYS = ["store_id", "sku"]
CATS = ["store_id", "sku", "dow", "month"] # Variables que LightGBM amará

def make_features(df):
    """Bloque matemático: Fechas, Lags y Promedios Móviles"""
    df = df.sort_values(KEYS + ["date"]).reset_index(drop=True)
    
    df["dow"] = df["date"].dt.dayofweek.astype("int8")
    df["month"] = df["date"].dt.month.astype("int8")
    
    grp = df.groupby(KEYS)["sales"]
    
    # Lags (Rezagos)
    for lag in [1, 7, 14, 28]:
        df[f"lag_{lag}"] = grp.shift(lag)
    
    # Promedios móviles (El shift(1) evita ver el futuro)
    grp_shift = df.assign(tmp=grp.shift(1)).groupby(KEYS)["tmp"]
    for w in [7, 14, 28]:
        df[f"roll_mean_{w}"] = grp_shift.transform(lambda x: x.rolling(w, min_periods=1).mean())
        
    return df

def main():
    # --- 2. LEER Y LIMPIAR ---
    df = pd.read_csv("data/train.csv")
    df["date"] = pd.to_datetime(df["date"])
    # df = df.rename(columns={"store_nbr": "store_id", "family": "sku"}) # Descomentar si es necesario

    # --- 3. EL PANEL (Rellenar huecos de tiempo) ---
    fechas = pd.date_range(df["date"].min(), df["date"].max())
    idx = pd.MultiIndex.from_product(
        [df["sku"].unique(), df["store_id"].unique(), fechas], 
        names=["sku", "store_id", "date"]
    )
    df = df.set_index(["sku", "store_id", "date"]).reindex(idx).reset_index()

    # --- 4. IMPUTACIÓN (La regla del Retail) ---
    df["sales"] = df["sales"].fillna(0.0) 
    if "promo" in df.columns: 
        df["promo"] = df["promo"].fillna(0)
    
    # Aplicar matemáticas y botar nulos iniciales
    df = make_features(df)
    df = df.dropna(subset=["lag_28"]).copy()
    
    # Vacuna Categórica: Definir el ADN del diccionario
    for c in CATS:
        df[c] = df[c].astype("category")

    # --- 5. ENTRENAMIENTO ---
    # RECORDAR: ¡Nunca meter el 'id', 'date' ni 'sales' a las features!
    features = [c for c in df.columns if c not in ["sales", "date", "id"]]
    cutoff = df["date"].max() - pd.Timedelta(days=28)
    
    train = df[df["date"] <= cutoff]
    valid = df[df["date"] > cutoff]

    model = lgb.LGBMRegressor(n_estimators=1000, objective="poisson", random_state=42)
    model.fit(
        train[features], train["sales"], 
        eval_set=[(valid[features], valid["sales"])], 
        callbacks=[lgb.early_stopping(50)]
    )

    # --- 6. FORECAST RECURSIVO ---
    work = df.copy()
    # Guardamos la última promo conocida para usarla en el futuro
    static = work.groupby(KEYS)[["promo"]].last().reset_index() if "promo" in work.columns else work[KEYS].drop_duplicates()
    preds = []

    for d in pd.date_range(work["date"].max() + pd.Timedelta(days=1), periods=100):
        # Cortar a 60 días para no ahogar la RAM
        hist = work[work["date"] >= d - pd.Timedelta(days=60)].copy()
        
        # Armar el día de "hoy" (futuro)
        today = static.copy()
        today["date"] = d
        today["sales"] = np.nan
        
        # Calcular features de este día pegándolo a la historia reciente
        tmp = make_features(pd.concat([hist, today], ignore_index=True))
        day_df = tmp[tmp["date"] == d].copy()
        
        # HEREDAR CATEGORÍAS (Para que LightGBM no prediga puros ceros)
        for c in CATS: 
            day_df[c] = day_df[c].astype(df[c].dtype)
        
        # Predecir y evitar ventas negativas
        y_hat = np.maximum(model.predict(day_df[features]), 0)
        
        # Inyectar predicción y guardar
        today["sales"] = y_hat
        work = pd.concat([work, today], ignore_index=True)
        
        day_df["y_pred"] = y_hat
        preds.append(day_df)

    # --- 7. EXPORTAR ---
    final_df = pd.concat(preds, ignore_index=True)[KEYS + ["date", "y_pred"]]
    final_df.to_csv("forecast_100d.csv", index=False)
    print("¡Misión Cumplida! Archivo guardado.")

if __name__ == "__main__":
    main()
