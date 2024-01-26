# Tarea 1a (semana 2)

1. Descargar el conjunto de datos `winequality-red.csv`. Se puede descargar desde [aquí](https://archive.ics.uci.edu/dataset/186/wine+quality) o desde [aquí](https://raw.githubusercontent.com/jealcalat/AEM-ITESO/main/datasets/winequality_red.csv).
2. Indicar cuáles son las variables numéricas y cuáles son las categóricas.
3. Realizar un gráfico pairsplot de todas las variables numéricas.
4. Calcular los estadísticos descriptivos para la variable `alcohol.` Separarlos por estadísticos de tendencia central y de dispersión.
5. Usar StandardScaler de Scikit-Learn para estandarizar dos variables numéricas de su elección. Comparar los estadísticos descriptivos de las variables originales y las estandarizadas con histogramas.
6. Usar MinMaxScaler Scikit-Learn para estandarizar dos variables numéricas de su elección. Comparar los estadísticos descriptivos de las variables originales y las estandarizadas con histogramas.


Referencias:

- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

# Tarea 2a (semana 3)

7. Obtener una matriz de correlaciones de todas las variables numéricas excepto `quality`.
8. Ordenar en orden descendente las correlaciones con respecto a `density`.
9. Seleccionar aquellas variables cuyo valor absoluto de correlación con respecto a `density` sea mayor o igual a 0.4.
10. ¿De qué variables depende (linealmente) *más* la densidad?