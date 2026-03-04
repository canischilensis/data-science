import pandas as pd
import numpy as np
import pytest
from main import make_features 

def test_retail_pipeline():
    df_raw = pd.DataFrame({
        "date": pd.to_datetime(["2017-01-01", "2017-01-03"]), # Falta el día 02
        "sku": [1, 1],
        "store_id": [10, 10],
        "sales": [10.0, 30.0],
        "id": [999, 1000] # El intruso que debemos ignorar
    })

    fechas = pd.date_range(df_raw.date.min(), df_raw.date.max())
    idx = pd.MultiIndex.from_product([[1], [10], fechas], names=["sku", "store_id", "date"])
    df_panel = df_raw.set_index(["sku", "store_id", "date"]).reindex(idx).reset_index()

    df_panel["sales"] = df_panel["sales"].fillna(0.0)

    df_feat = make_features(df_panel)

    assert len(df_panel) == 3, "Error: El panel no rellenó los días faltantes"

    assert df_panel.loc[1, "sales"] == 0.0, "Error: El nulo no se convirtió en cero ventas"
    
    assert df_feat.loc[2, "lag_1"] == 0.0, "Error: El cálculo de lags falló"

    print("✅ ¡Pipeline validado con éxito!")
