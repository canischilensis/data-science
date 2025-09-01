# Clustering con K-Means: Ejercicio de Segmentación y Análisis de Datos

Este proyecto implementa el algoritmo de **K-Means** para la segmentación de datos, explorando diferentes valores de *k* y evaluando la calidad de los clústeres mediante métricas y visualizaciones.

---

## 📑 Índice
1. [Objetivo del Proyecto](#objetivo-del-proyecto)
2. [Datos Utilizados](#datos-utilizados)
3. [Metodología](#metodología)
   - 3.1 Preprocesamiento de datos  
   - 3.2 Aplicación de K-Means  
   - 3.3 Evaluación del número óptimo de clústeres  
4. [Resultados](#resultados)
5. [Visualizaciones](#visualizaciones)
6. [Conclusiones](#conclusiones)
7. [Requisitos](#requisitos)
8. [Ejecutar el Notebook](#ejecutar-el-notebook)

---

## 🎯 Objetivo del Proyecto
Categorizar perfiles de estudiantes según sus niveles de estrés mediante **técnicas de clustering (K-means)**, con el fin de comprender los factores psicológicos, sociales y académicos que inciden en su bienestar.

---

## 📊 Datos Utilizados
- Dataset: *[indica aquí el nombre del dataset cargado en el notebook]*  
- Variables: *[especifica brevemente las columnas más importantes analizadas]*  

---

## 🛠️ Metodología

### 3.1 Preprocesamiento de datos
- Carga de datos con **Pandas**.  
- Exploración inicial (head, info, describe).  
- Normalización / estandarización de variables si fue necesario.  

### 3.2 Aplicación de K-Means
- Uso de la implementación de `sklearn.cluster.KMeans`.  
- Prueba de distintos valores de **k**.  

### 3.3 Evaluación del número óptimo de clústeres
- **Método del Codo** (Inertia).  
- **Coeficiente Silhouette**.  

---

## 📈 Resultados
- Identificación del número óptimo de clústeres.  
- Etiquetado de cada observación según su clúster asignado.  
- Métricas de desempeño y comparación entre valores de *k*.  

---

## 📉 Visualizaciones
Incluye gráficos generados en el notebook:
- Método del Codo.  
- Silhouette Score.  
- Gráficos de dispersión coloreados por clústeres.  

---

## ✅ Conclusiones
El análisis comparativo de los modelos de clustering con k=3, k=4 y k=5 permitió identificar diferencias significativas en la forma de segmentar a los estudiantes según su nivel de estrés y características asociadas. Con k=3, la clasificación se ajusta al esquema tradicional de bajo, medio y alto estrés, lo cual facilita la interpretación general, pero genera solapamientos, especialmente entre los niveles medio y alto. Con k=5, el método silhouette logra una separación más fina y distingue subgrupos intermedios (ej. estrés académico o perfiles emocionales específicos), pero la complejidad de interpretación aumenta, lo que puede dificultar la aplicación práctica. En cambio, el modelo con k=4 ofrece un equilibrio óptimo: la visualización con PCA mostró clusters bien definidos y el heatmap evidenció perfiles diferenciados entre estrés alto con vulnerabilidad, estrés moderado con autoestima protectora, estrés leve, y bajo estrés con alta resiliencia. Por lo tanto, el modelo de cuatro clusters representa la solución más adecuada, al aportar tanto claridad interpretativa como riqueza en la caracterización de perfiles, lo que resulta especialmente útil para diseñar intervenciones de apoyo más focalizadas.  

---

## 📦 Requisitos
Librerías necesarias:
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  

Instalación rápida:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
