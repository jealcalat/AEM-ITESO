# Tarea 3, Parte 1

## Obtener MLE de forma analítica

1. Suponer que $X_1, X_2, \ldots, X_n$ son variables aleatorias independientes e idénticamente distribuidas con distribución exponencial con parámetro $\lambda$. La función de densidad exponencial está dada por 

$$f(x) = \lambda e^{-\lambda x},\quad \text{para } x \geq 0, \lambda > 0$$

a. Obtener la función de verosimilitud para $\lambda$.

b. Mostrar que el estimador de máxima verosimilitud de $\lambda$ es $\mathbf{E}[X]$.

## Obtener MLEs de forma numérica

2. Usando la función de densidad exponencial:

a. Simula $n = 1000$ observaciones de una distribución exponencial con $\lambda = 2$ (para darle reproducibilidad a los resultados, en Python puedes usar `np.random.seed(123)` antes de generar las observaciones).

b. Define la función de verosimilitud negativa para $\lambda$.

c. Con la función `minimize` de `scipy.optimize` encuentra el estimador de máxima verosimilitud de $\lambda$. Recuerda las restriccion de $\lambda$. Usa el método apropiado para este caso en el argumento `method` de `minimize`.

3. Descarga el dataset de cáncer:

```python
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer(as_frame=True)
y = data.target
data = data.data

data.describe()
```

a. Visualiza la distribución de la primera variable (`mean radius`).

b. Escoge un modelo para esta variable y encuentra los parámetros de este modelo usando MLE. Tip: podría ser más de una distribución, en cuyo caso podrías usar una mezcla de distribuciones. Recuerda la forma general de un modelo de mezcla de distribuciones:

$$f(x) = \sum_{i=1}^k \pi_i f_i(x)$$

en donde $\pi_i$ es la probabilidad de que la observación $x$ provenga de la distribución $i$ y 

$$\sum_{i=1}^k \pi_i = 1$$

En este caso, $k$ es el número de distribuciones que estás usando en la mezcla (por ejemplo, $k = 2$ si estás usando una mezcla de dos distribuciones, en cuyo caso, $\pi_1=1-\pi_2$). $f_i(x)$ es la función de densidad de la distribución $i$. Por ejemplo, si estás usando una mezcla de dos distribuciones exponenciales, entonces $f_1(x)$ es la función de densidad de la primera distribución exponencial y $f_2(x)$ es la función de densidad de la segunda.