# Tarea 3, Parte 2

### Ejercicio de regresión lineal múltiple

**Contexto**: utilizaremos el conjunto de datos de Boston Housing para predecir el valor medio de las viviendas en los suburbios de Boston en función de diversas características, como la tasa de criminalidad, la cantidad de habitaciones, etc.

#### Cargando conjunto de datos

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing
# Load the california housing dataset
housing = fetch_california_housing()
# Convert to DataFrame for better visualization
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MEDV'] = housing.target
print(df.head())
```

#### Preguntas

1. ¿Cuáles son las características más importantes que afectan el valor medio de una casa en los suburbios de Boston? Usar la matriz de correlación para identificarlas.
2. Ajuste un modelo de regresión lineal múltiple y calcule el valor de R cuadrado. ¿Qué tan bien se ajusta el modelo a los datos?
3. Dada una casa con `HouseAge = 15`, `AveRooms = 5`, `AveBedrms = 2`, `Population = 15`, `AveOccup = 3` y el resto de variables promedio, ¿cuál sería el valor mediano previsto de las viviendas?

### Ejercicio de regresión logística

**Contexto**: utilizar el conjunto de datos sobre cáncer de mama para predecir si una masa mamaria es maligna o benigna en función de características como el radio medio, la textura, etc.

#### Cargando conjunto de datos

```python
from sklearn.datasets import load_breast_cancer

# Load the Breast Cancer dataset
cancer = load_breast_cancer()

# Convert to DataFrame for better visualization
df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df_cancer['target'] = cancer.target

# Display first 5 rows
print(df_cancer.head())
```

#### Preguntas

1. Ajuste un modelo de regresión logística con cuatro variables (`mean radius`, `mean texture`, `mean perimeter`, `mean area`) y calcula la precisión. ¿Qué tan bien clasifica el modelo a las masas?
2. ¿Qué variables afectan positivamente la probabilidad de que una masa sea maligna? ¿Cuáles afectan negativamente?
3. Dada una nueva masa con las siguientes características `[21.99, 12.38, 124, 1001]`, ¿cuál es la probabilidad de que esta masa sea maligna?
