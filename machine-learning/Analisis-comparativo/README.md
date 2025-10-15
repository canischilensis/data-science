# Análisis comparativo de modelos: Clasificación y Regresión (German Credit – UCI)

Este repositorio contiene dos notebooks de análisis predictivo (clasificación y regresión) basados en el **dataset German Credit (UCI Statlog)**. El objetivo es comparar distintos modelos, documentar el preprocesamiento, justificar las métricas de evaluación y reportar los resultados con buenas prácticas de ciencia de datos (EDA, preparación de datos, validación y tuning básico).

> Notebooks incluidos:
> - `Analisis-comparativo-modelo-clasificacion.ipynb`
> - `Analisis-comparativo-modelo-regresion.ipynb`

---

## 1) Problemas abordados

### 1.1 Clasificación (riesgo crediticio)
- **Variable objetivo:** `default` (0 = buen pagador, 1 = mal pagador).
- **Meta:** detectar correctamente a clientes con **alto riesgo** (clase 1).  
- **Énfasis:** recordatorio (recall) de la clase positiva y métricas robustas ante desbalance (PR-AUC).

### 1.2 Regresión (monto de crédito)
- **Variable objetivo:** `credit_amount` (monto del crédito solicitado).  
- **Meta:** estimar el monto a partir de atributos demográficos, laborales y de historial crediticio.

---

## 2) Dataset y variables

- **Fuente:** German Credit (UCI).  
- **Observaciones:** 1.000 casos con variables demográficas/económicas y de comportamiento crediticio.
- **Ejemplos de variables:**
  - Numéricas: `duration_in_month`, `credit_amount`, `installment_as_income_perc`, `age`, etc.
  - Categóricas: `purpose`, `housing`, `saving_accounts`, `checking_status`, `personal_status_sex` (se **fragmenta** en *sexo* y *estado civil*), etc.

> En el cuaderno se muestran:
> - Tratamiento de valores nulos.
> - **Label Encoding** y **One-Hot Encoding**.
> - Separación de `personal_status_sex` en dos campos (sexo / estado civil).
> - Estadística descriptiva y *insights* (p. ej., relación moderada-alta entre `credit_amount` y `duration_in_month`).

---

## 3) Metodología de trabajo

### 3.1 Preprocesamiento
- Imputación de faltantes (según tipo de variable).
- Codificación de categóricas: **Label Encoding** (para ordinales) y **One-Hot Encoding** (para nominales).
- Escalado comparado: **StandardScaler**, **RobustScaler** y **MinMaxScaler** (según sensibilidad a *outliers* y modelo).
- Revisión de distribución (normalidad) y correlaciones (Pearson/Spearman/Kendall).

### 3.2 Validación y evaluación
- **Partición:** *train/test* + validación con **KFold** / **StratifiedKFold** (en clasificación).
- **Métricas de clasificación (clase positiva = `default=1`):**
  - **Recall** (prioridad), **Precision**, **F1**, **PR-AUC** (idónea en desbalance), **ROC-AUC** (referencia).
- **Métricas de regresión:** **MAE**, **RMSE**, **R²** (se reportan valores *median/std* cuando procede).
- **Desbalance:** uso de `class_weight='balanced'` en modelos lineales/no lineales y **ajuste de umbral** de decisión para optimizar *trade-offs* (recall vs precision).

### 3.3 Modelos comparados (según notebook)
- **Clasificación:** Regresión Logística, **SVM (RBF)**, KNN.  
- **Regresión:** **Regresión Lineal**, Árbol de Regresión, **SVR (RBF)**.  
- (En el análisis se discute por qué descartar/aceptar cada enfoque y el impacto del escalado).

---

## 4) Resultados principales

### 4.1 Clasificación (riesgo crediticio)
- **Mejor modelo global:** **SVM (RBF con umbral optimizado)**  
  - Resultados reportados en test (clase `default=1`):  
    - **Recall ≈ 0.67**, **Precision ≈ 0.61**, **F1 ≈ 0.64**  
    - **ROC-AUC ~ 0.80** (PR-AUC reportada en torno a ~0.65 en el análisis)  
  - Motivo: mejor equilibrio para **reducir falsos negativos** (riesgo de alto costo) sin disparar falsos positivos.

- **Alternativa interpretable:** **Regresión Logística**  
  - Desempeño cercano al SVM, **ROC-AUC ~ 0.74**; ventajosa si se requiere **explicabilidad** (coeficientes, odds ratios).

- **Modelo descartado:** **KNN**  
  - Bajo *recall* en la clase minoritaria; sensible al escalado y a la densidad local de datos.

> Conclusión operativa: si la prioridad es **minimizar morosos no detectados**, usar **SVM (RBF + umbral)**; si se privilegia **explicabilidad** y despliegue sencillo, **Regresión Logística**.

### 4.2 Regresión (monto del crédito)

| Modelo                | MAE (med) | MAE (std) | RMSE (med) | R² (med) |
|----------------------|-----------:|----------:|-----------:|---------:|
| **Regresión Lineal** | **1301.14**| **49.08** | **1867.33**| **0.56** |
| Árbol de Regresión   | 1367.06    | 59.52     | 2106.07    | 0.43     |
| SVR (RBF)            | 1647.24    | 91.52     | 2679.91    | 0.09     |

- **Mejor modelo:** **Regresión Lineal** por menor error (MAE/RMSE) y **R² ~ 0.56**.  
- **Árbol:** interpretabilidad por reglas, pero pierde precisión global.  
- **SVR (RBF):** no se adapta bien al patrón del dataset (en las condiciones evaluadas).

> *Insight EDA:* la relación más fuerte es **`credit_amount` ↔ `duration_in_month`** (Pearson/Spearman ~0.625). Tiene sentido económico: créditos mayores suelen requerir más meses de pago.

---

## 5) Estructura del repositorio

```
.
├── Analisis-comparativo-modelo-clasificacion.ipynb
├── Analisis-comparativo-modelo-regresion.ipynb
└── README.md  ← (este archivo)
```

---

## 6) Requisitos e instalación

**Python 3.10+** recomendado. Paquetes clave usados en los notebooks:

- `pandas`, `numpy`
- `scikit-learn` (modelado, métricas, validación)
- `scipy` / `statsmodels` (pruebas estadísticas)
- `matplotlib`, `seaborn` (gráficos)
- `skopt` (en el notebook de regresión se menciona para *Bayesian search*)

Instala con:

```bash
pip install -U pandas numpy scikit-learn scipy statsmodels matplotlib seaborn scikit-optimize
```

> Si requieres **reproducibilidad exacta**, crea un entorno virtual y congela dependencias:
> ```bash
> python -m venv .venv
> source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
> pip install -r requirements.txt  # si generas este archivo
> ```

---

## 7) Cómo ejecutar

1. Clona/descarga el repo.
2. Abre los notebooks con Jupyter o VS Code:
   ```bash
   jupyter lab
   # o
   jupyter notebook
   ```
3. Ejecuta cada celda en orden.  
   - El notebook de **clasificación** muestra EDA → preparación → validación estratificada → ajuste de umbral → reporte de métricas y recomendaciones.  
   - El notebook de **regresión** muestra EDA → preparación → evaluación con KFold → comparación de modelos.

---

## 8) Decisiones técnicas y buenas prácticas

- **Desbalance** (clasificación): uso de `class_weight='balanced'` y **optimización de umbral** con curvas PR/ROC para alinear la métrica de negocio (minimizar FN).
- **Escalado**: comparación entre `StandardScaler`, `RobustScaler`, `MinMaxScaler` según sensibilidad del algoritmo; SVM/SVR requieren escalado consistente.
- **Codificación de categóricas**: OHE para nominales; Label Encoding o mapeos para ordinales.
- **Validación**: `KFold` / `StratifiedKFold` para estimar rendimiento fuera de muestra; *reportar test* por separado.
- **Explicabilidad**: cuando el modelo es caja negra (p. ej., SVM RBF), se recomienda agregar **coeficientes/log-odds** (en LogReg), o **SHAP**/permutaciones (futuro) para *feature importance*.

---

## 9) Limitaciones y trabajo futuro

- **Feature engineering** adicional: interacciones, transformaciones no lineales, *binning* de montos/edades, variables de estabilidad laboral, etc.
- **Tuning sistemático**: `GridSearchCV`/`BayesSearchCV` con espacios de hiperparámetros mejor definidos (especialmente para SVM/SVR).
- **Curvas de costo**: incorporar **cost-sensitive learning** (matriz de costos) para el negocio crediticio.
- **Modelos extra**: *Tree ensembles* (Random Forest, Gradient Boosting, XGBoost/LightGBM) y calibración de probabilidades.
- **Explicabilidad global/local**: SHAP/LIME para decisiones individuales y *feature attributions*.

---

## 10) Licencia y uso de datos

- **Datos**: German Credit Dataset (UCI Statlog). Revise condiciones de uso de la UCI Machine Learning Repository.  
- **Código**: si no se especifica, se sugiere licenciar bajo **MIT** o similar (agrega `LICENSE` según preferencia).

---

## 11) Contacto

Para dudas, mejoras o colaboración, abre un *issue* o *pull request* en el repositorio correspondiente.

--- 

> **Resumen ejecutivo**
> - **Clasificación:** SVM (RBF + umbral) logra el **mejor balance** (Recall≈0.67, F1≈0.64, ROC-AUC~0.80) para capturar morosos; LogReg es la alternativa **más interpretable** (ROC-AUC~0.74).  
> - **Regresión:** **Regresión Lineal** domina (MAE≈1301, RMSE≈1867, R²≈0.56).  
> - **EDA relevante:** la correlación más fuerte es **monto ↔ duración**, consistente con el dominio financiero.
