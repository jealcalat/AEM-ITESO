import marimo

__generated_with = "0.9.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        # Time Regulation Model
        En la psicología experimental existe un modelo animal para la impulsividad de acción. Se suele probar con una tarea experimental llamada _Reforzamiento Diferencial de Tasa Bajas_. Básicamente consiste en lo siguiente: se mete a un animala  una caja experimental, y tiene que esperar una cantidad de tiempo fija, digamos 15 segundos, y responder por comida. Si responde antes se castiga y el contador de tiempo se reinicia, teniendo que esperar de nuevo los 15 segundos (más lo que haya tardado anteriormente). Si en un intento respondió a los 10 segundos, deberá esperar otros 15 adicionales para poder recibir alimento. La impulsividad aquí se refiere al hecho de que el animal debe aprender a refrenar sus acciones, de otra manera no recibe su recompensa. 
        """
    )
    return


@app.cell(hide_code=True)
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    import numpy as np
    from scipy.optimize import minimize
    from scipy.stats import gamma, expon
    import matplotlib.pyplot as plt
    import pandas as pd
    return expon, gamma, minimize, np, pd, plt


@app.cell
def __(pd):
    datos = pd.read_csv("datasets/datos_muestra.csv", names=['irt'], header=None)
    datos

    return (datos,)


@app.cell
def __(datos, plt):
    plt.hist(datos, bins=30);
    plt.show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Los datos se han modelado, de hecho, como una mezcla de dos funciones: una exponencial y una gamma (aunque bien se podría modelar con una exponencial y una normal).

        $$
        f(y \mid q, \lambda, \text{scale}, \text{shape}) = q \cdot f_{\text{Gamma}}(y \mid \text{shape}, \text{scale}) + (1 - q) \cdot f_{\text{Exp}}(y \mid \lambda)
        $$
        """
    )
    return


if __name__ == "__main__":
    app.run()
