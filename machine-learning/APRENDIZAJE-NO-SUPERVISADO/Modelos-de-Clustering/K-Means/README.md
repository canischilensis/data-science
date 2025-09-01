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
Aplicar el algoritmo de **K-Means Clustering** para agrupar datos de manera no supervisada y analizar cómo varía la calidad de los grupos según el número de clústeres elegidos.  

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
- *[Agrega aquí las conclusiones principales: por ejemplo, cuál fue el valor óptimo de k y qué insights aportó la segmentación]*.  

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
