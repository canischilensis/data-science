# 📋 Tablero Kanban: Estrategia Titanic con TensorFlow Decision Forests (TF-DF)

## 📌 Sección 1: Configuración y Pipeline de Datos (ETL)

**Título Técnico:** *Data Ingestion & TF-DF Native Preprocessing*

Esta fase prepara el entorno para que TensorFlow pueda "leer" los datos crudos, especialmente el texto, sin necesidad de One-Hot Encoding manual excesivo.

- [x] **Instalación de Dependencias:** Instalar `tensorflow_decision_forests`, `pandas`, `numpy`. Verificar versión de TF-DF.
* [x] **Ingesta de Datos:** Cargar `train.csv` y `test.csv` usando Pandas.
* [ ] **Feature Engineering (Python-side):** Crear función `preprocess(df)`:
* Normalizar nombres (eliminar puntuación).
* Parsear `Ticket`: Separar el prefijo (item) del número.


* [ ] **Conversión a TF Dataset:** Usar `tfdf.keras.pd_dataframe_to_tf_dataset` especificando la etiqueta `label="Survived"`.
* [ ] **Tokenización Nativa:** Implementar función `tokenize_names` usando `tf.strings.split`.
* *Objetivo:* Convertir "Braund, Mr. Owen Harris" en una lista `["Braund", "Mr", "Owen", "Harris"]` que el modelo consumirá directamente.



## 📌 Sección 2: Arquitectura del Modelo Base y Cortes Oblicuos

**Título Técnico:** *Gradient Boosted Trees (GBT) with Sparse Oblique Splits*

Aquí nos alejamos del Random Forest clásico y configuramos un **Gradient Boosted Tree** capaz de entender geometría compleja.

* [ ] **Inicialización GBT:** Instanciar `tfdf.keras.GradientBoostedTreesModel`.
* [ ] **Configuración de Cortes Oblicuos (Clave del Éxito):**
* Fijar `split_axis="SPARSE_OBLIQUE"`.
* Configurar `sparse_oblique_normalization="MIN_MAX"`.
* Configurar `sparse_oblique_num_projections_exponent=2.0`.
* *Por qué:* Esto permite al árbol hacer cortes diagonales matemáticos en lugar de solo rectos.


* [ ] **Parámetros de Regularización Manual:**
* Fijar `min_examples=1` (para aprender patrones muy finos).
* Fijar `shrinkage=0.05` (tasa de aprendizaje lenta para mayor precisión).
* Fijar `num_trees=2000`.



## 📌 Sección 3: Optimización Automatizada de Hiperparámetros

**Título Técnico:** *Automated Hyperparameter Tuning via Random Search*

En lugar de adivinar, usamos fuerza bruta computacional para encontrar la "receta perfecta".

* [ ] **Configurar el Tuner:** Instanciar `tfdf.tuner.RandomSearch(num_trials=1000)`.
* [ ] **Definir Espacio de Búsqueda (Search Space):**
* Añadir opciones para `min_examples` [2, 5, 7, 10].
* Añadir opciones para `categorical_algorithm` ["CART", "RANDOM"].
* Añadir opciones para `growing_strategy` ["LOCAL", "BEST_FIRST_GLOBAL"].
* Añadir opciones para `max_depth` [3, 4, 5, 6, 8].


* [ ] **Entrenamiento con Tuning:** Ejecutar `tuned_model.fit(train_ds, tuner=tuner)`.
* *Meta:* Dejar que el modelo pruebe 1000 combinaciones y elija la mejor automáticamente.



## 📌 Sección 4: Estrategia de Ensamblaje Masivo (Bagging)

**Título Técnico:** *Large-Scale Ensemble with Honest Trees*

Esta es la **"Salsa Secreta"** del notebook para obtener ese puntaje alto y evitar el Overfitting.

* [ ] **Crear Bucle de Ensamblaje:** Diseñar un loop `for i in range(100)` para entrenar 100 modelos distintos.
* [ ] **Configurar "Honest Trees":**
* Dentro del loop, instanciar el modelo con `honest=True`.
* *Concepto:* Usa un set de datos para crear la estructura del árbol y otro diferente para los valores de las hojas (reduce sesgo).


* [ ] **Diversificación por Semilla:** Asignar `random_seed=i` en cada iteración para asegurar que cada modelo vea una variante distinta del caos.
* [ ] **Entrenamiento Iterativo:** Entrenar cada uno de los 100 modelos dentro del loop.

## 📌 Sección 5: Inferencia y Agregación

**Título Técnico:** *Inference Aggregation & Thresholding*

Cómo combinar las 100 "opiniones" de los modelos para tomar la decisión final.

* [ ] **Acumulación de Predicciones:** Crear variable `predictions` y sumar las probabilidades de salida de cada uno de los 100 modelos.
* [ ] **Promedio (Averaging):** Dividir la suma total entre 100 (`predictions /= num_predictions`).
* [ ] **Thresholding (Corte):** Aplicar la lógica binaria: Si `promedio >= 0.5` entonces 1 (Vive), sino 0 (Muere).
* [ ] **Generación de Submission:** Crear DataFrame con `PassengerId` y `Survived` y exportar a CSV.