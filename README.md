
# 📊 Data Science & Machine Learning Portfolio

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R%20%2F%20RStudio-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

Repositorio personal que centraliza mi trabajo y aprendizaje en **Ciencia de Datos**, **Estadística Aplicada** y **Machine Learning**.
Incluye notebooks y recursos que van desde fundamentos (probabilidad, inferencia, pruebas de hipótesis) hasta modelos supervisados/no supervisados, reducción de dimensionalidad (PCA) y análisis de eficiencia (**DEA**), además de reportes en **RMarkdown**.

---

## 🧭 Contenido rápido (si vienes por portafolio)
- **Quiero ver modelos “de verdad”** → ve a: [`/machine-learning`](./machine-learning)
- **Quiero ver análisis estadístico + decisiones** → ve a: [`/estadistica`](./estadistica)
- **Quiero ver EDA + eficiencia (DEA)** → ve a: [`/estadistica/eficiencia/DEA`](./estadistica/eficiencia/DEA)
- **Quiero ver dominio de librerías base** → ve a: [`/Librerias`](./Librerias)
- **Quiero ver R + reportes reproducibles** → ve a: [`/R-studio`](./R-studio)
- **Quiero ver ejercicios guiados (Microsoft Learn)** → ve a: [`/microsoft-learn`](./microsoft-learn)

---

## 🗂️ Estructura del repositorio

> Diseño modular para navegar por **teoría → práctica → proyectos**.

- **`/data`**: datasets en `.csv`/`.xlsx` usados por varios notebooks.
- **`/estadistica`**: probabilidad, distribuciones, inferencia, pruebas de hipótesis y DEA (eficiencia).
- **`/machine-learning`**: aprendizaje supervisado/no supervisado, PCA y ejercicios aplicados.
- **`/Librerias`**: notebooks tipo “cheatsheet” (NumPy/Pandas/Matplotlib/Seaborn).
- **`/R-studio`**: análisis y reportes en RMarkdown (`.Rmd`) + salidas en HTML.
- **`/microsoft-learn`**: laboratorios prácticos (ruta de aprendizaje).

---

## 🚀 Proyectos destacados (selección)

> Tabla pensada para que un reclutador encuentre rápido “lo mejor”.

| Proyecto | Tipo | Qué demuestra | Ruta |
|---|---|---|---|
| **Predicción de riesgo crediticio** | Clasificación (Reg. Logística) | Feature engineering, preparación de datos, modelo + evaluación | `machine-learning/aprendizaje-supervisado/Regresión/Regresion-logistica/Analisis-Prediccion-riesgo-crediticio/` |
| **Análisis de calidad de vino (tinto/blanco)** | Regresión | EDA, modelado y conclusiones sobre variables fisicoquímicas | `machine-learning/aprendizaje-supervisado/Regresión/` → `vino-blanco/` y `vino-tinto/` |
| **Segmentación por estrés (K-Means)** | Clustering | Normalización, elección de k, interpretación de clusters | `machine-learning/APRENDIZAJE-NO-SUPERVISADO/Modelos-de-Clustering/K-Means/` |
| **PCA aplicado (Palmer Penguins)** | Reducción de dimensionalidad | PCA + visualización + lectura de componentes | `machine-learning/Tecnicas-Reduccion-de-Dimensionalidad/PCA/PCA-Penguins-Palmer/` |
| **DEA + EDA en Retail (ventas minoristas)** | Eficiencia (DEA) | EDA, construcción de DMUs y comparación de eficiencia | `estadistica/eficiencia/DEA/retail-EDA-DEA/` |
| **DEA + EDA Retail Bike** | Eficiencia (DEA) | Análisis exploratorio + eficiencia aplicada a retail | `estadistica/eficiencia/DEA/retail-bike-DEA-EDA/` |
| **DEA + EDA Taxis** | Eficiencia (DEA) | EDA + análisis de eficiencia en transporte/servicios | `estadistica/eficiencia/DEA/taxis-EDA-DEA/` |
| **Air Quality: PCA + EDA + DEA** | Eficiencia + PCA | Integración PCA (reducción) con medición de eficiencia | `estadistica/eficiencia/DEA/air-quality-PCA-EDA-DEA/` |
| **Indicadores globales + predicción esperanza de vida** | Data analysis / predicción | Tendencias macro, limpieza, análisis y predicción | `estadistica/eficiencia/DEA/Indicadores-Socioeconómicos-Demográficos-Globales/` |
| **Diabetes (clasificación / regresión)** | Supervisado | Árboles/Regresión con dataset clínico | `machine-learning/aprendizaje-supervisado/Clasificación/Arboles-de-decision/diabetes/` y `machine-learning/aprendizaje-supervisado/Regresión/Regresion-lineal/diabetes/` |
| **Titanic Survival** | Clasificación | Pipeline clásico de ML con dataset histórico | `machine-learning/aprendizaje-supervisado/Clasificación/Arboles-de-decision/Titanic/` |
| **Predicción de salario** | Regresión lineal | Modelo simple + lectura de coeficientes | `machine-learning/aprendizaje-supervisado/Regresión/Regresion-lineal/salario/` |
| **Serie temporal simple (tiempo vs hora)** | Regresión | Lectura de archivos (csv/xlsx) + ajuste y predicción | `machine-learning/aprendizaje-supervisado/Regresión/Regresion-lineal/tiempo-vs-hora/` |

---

## 📈 Rutas de aprendizaje dentro del repo

### 1) 📌 Estadística & Probabilidad (`/estadistica`)
- Introducción, probabilidad y distribuciones
- Inferencia estadística y pruebas de hipótesis
- **Teoría del error** (mediciones, incertidumbre, rectificación)

Ruta: [`./estadistica`](./estadistica)

### 2) 🤖 Machine Learning (`/machine-learning`)
- **Supervisado**: regresión (simple/múltiple/logística), clasificación (árboles, etc.)
- **No supervisado**: K-Means
- **Reducción de dimensionalidad**: PCA

Ruta: [`./machine-learning`](./machine-learning)

### 3) 🧰 Librerías base (Python) (`/Librerias`)
- **NumPy**: arrays, reshape, operaciones vectorizadas
- **Pandas**: limpieza, nulos, filtrado, groupby, pivot/melt
- **Matplotlib/Seaborn**: visualización desde lo básico a lo analítico

Ruta: [`./Librerias`](./Librerias)

### 4) 🧾 Reportes en R (`/R-studio`)
- Reportes con **RMarkdown** y salidas HTML
- Análisis enfocados (ej. ventas retail)

Ruta: [`./R-studio`](./R-studio)

---

## 🛠️ Instalación y ejecución (local)

### 1) Clonar el repositorio
```bash
git clone https://github.com/diadasiachilensis/data-science.git
cd data-science
````

### 2) Crear y activar entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# En Windows: venv\Scripts\activate
```

### 3) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4) Abrir notebooks

```bash
jupyter notebook
# o
jupyter lab
```

---

## 📦 Tecnologías y stack (resumen)

* **Python**: análisis de datos, visualización y ML.
* **Jupyter Notebooks**: documentación + experimentación reproducible.
* **R / RStudio**: reportes en RMarkdown.
* Librerías habituales en este tipo de repos (según notebooks): `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `statsmodels`.

---

## ✅ Estándares de trabajo (cómo están construidos los notebooks)

En general, los notebooks siguen este flujo:

1. **Carga y limpieza** (control de nulos, tipos, outliers cuando aplica)
2. **EDA** (distribuciones, relaciones, insights)
3. **Modelado** (baseline → mejoras)
4. **Evaluación** (métricas + interpretación)
5. **Conclusiones** (decisiones y siguientes pasos)

---

## 🧩 Roadmap (mejoras planificadas)

* [ ] Agregar un “Índice de proyectos” con links directos a notebooks clave
* [ ] Normalizar nombres de carpetas (evitar tildes/espacios en rutas críticas)
* [ ] Incluir `Makefile` o scripts para ejecución rápida (setup + run)
* [ ] Añadir `pre-commit` (formato/lint) y export automático de notebooks a HTML/PDF
* [ ] Crear una carpeta `/docs` con capturas y resultados finales por proyecto

---

## ✒️ Autor

* GitHub: `diadasiachilensis`

---

### Nota

Este repositorio se mantiene en evolución como parte de mi formación continua y desarrollo de portafolio.
Si quieres ver “lo más demostrativo” primero, empieza por la tabla de **Proyectos destacados**.
