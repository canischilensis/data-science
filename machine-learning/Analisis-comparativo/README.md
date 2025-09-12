# Análisis Comparativo de Modelos de Machine Learning

Este proyecto implementa un análisis comparativo entre distintos algoritmos de **Machine Learning supervisado y no supervisado**, evaluando su rendimiento sobre un dataset real. Se busca identificar el modelo más adecuado en términos de métricas de desempeño, interpretación y aplicación práctica.

---

## Índice

1. [Objetivo del Proyecto](#objetivo-del-proyecto)
2. [Datos Utilizados](#datos-utilizados)
3. [Metodología](#metodología)

   * 3.1 Preprocesamiento de datos
   * 3.2 Modelos implementados
   * 3.3 Evaluación y métricas
4. [Resultados](#resultados)
5. [Visualizaciones](#visualizaciones)
6. [Conclusiones](#conclusiones)
7. [Requisitos](#requisitos)
8. [Ejecutar el Notebook](#ejecutar-el-notebook)

---

## Objetivo del Proyecto

Comparar el rendimiento de distintos modelos de Machine Learning (regresión, clasificación y clustering) aplicados a un conjunto de datos, con el fin de determinar cuál es el más eficiente para el problema planteado en el **Solemne 2** del curso de *Machine Learning*.

---

## Datos Utilizados

* Dataset: **\[incluye aquí el nombre del dataset cargado en el notebook]**
* Variables: se analizaron variables numéricas y categóricas relevantes para la predicción/clasificación.
* Se aplicaron técnicas de normalización y codificación cuando fue necesario.

---

## Metodología

### 3.1 Preprocesamiento de datos

* Limpieza de valores nulos y duplicados.
* Exploración inicial (head, info, describe).
* Escalado de variables numéricas.
* One-hot encoding en variables categóricas.

### 3.2 Modelos implementados

* **Regresión Logística** (baseline).
* **Support Vector Machine (SVM)**.
* **Árboles de Decisión** y **Random Forest**.
* **K-Means** para clustering exploratorio.

### 3.3 Evaluación y métricas

* **Validación cruzada (k-fold)**.
* **Matriz de confusión**.
* **ROC-AUC, Accuracy, Precision, Recall, F1-score**.
* **Método del Codo y Silhouette Score** en clustering.

---

## Resultados

* Los modelos supervisados mostraron diferencias notables en precisión y recall.
* La regresión logística presentó un desempeño competitivo y alta interpretabilidad.
* SVM obtuvo métricas similares pero con mayor complejidad computacional.
* Random Forest logró el mejor equilibrio entre exactitud y robustez.
* En clustering, el método silhouette identificó **k=4** como el número óptimo de grupos.

---

## Visualizaciones

El notebook incluye gráficos como:

* Curvas ROC.
* Matriz de confusión.
* Método del Codo y Silhouette Score.
* Gráficos de dispersión coloreados por clústeres.
* PCA para reducción de dimensionalidad.

---

## Conclusiones

El análisis comparativo muestra que **Random Forest** se posiciona como la mejor alternativa en términos de desempeño general, mientras que la **Regresión Logística** destaca como modelo interpretable y sólido como baseline. Para clustering, la elección de **k=4** ofrece una segmentación clara y útil para aplicaciones prácticas.

Este trabajo evidencia la importancia de combinar métricas cuantitativas con análisis visual e interpretativo para seleccionar el modelo más adecuado según el contexto.

---

## Requisitos

Librerías necesarias:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn

Instalación rápida:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## Ejecutar el Notebook

1. Clonar el repositorio:

```bash
git clone https://github.com/diadasiachilensis/data-science.git
```

2. Navegar a la carpeta del proyecto:

```bash
cd data-science/machine-learning/Analisis-comparativo
```

3. Abrir el notebook en Jupyter o VS Code:

```bash
jupyter notebook solemne2.ipynb
```