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
    from scipy.stats import norm, expon
    import matplotlib.pyplot as plt
    import pandas as pd
    return expon, minimize, norm, np, pd, plt


@app.cell
def __(pd):
    datos = pd.read_csv("datasets/datos_muestra.csv", names=['irt'], header=None)
    datos

    return (datos,)


@app.cell
def __(datos, plt):
    plt.hist(datos['irt'], bins=30);
    plt.axvline(2, color='red')
    plt.show()

    return


@app.cell
def __(mo):
    mo.md(
        r"""
        Los datos se han modelado, de hecho, como una mezcla de dos funciones: una exponencial y una gamma (aunque bien se podría modelar con una exponencial y una normal).

        $$
        f(y \mid \pi, \lambda, \mu, \sigma) = \pi \cdot f_{\text{normal}}(y \mid \mu, \sigma) + (1 - \pi) \cdot f_{\text{Exp}}(y \mid \lambda)
        $$
        """
    )
    return


@app.cell
def __(expon, norm, np):
    def TimeReg_neg_log_lik(param, y):
        pi, lam, mu, sig = param
        norm_pdf = pi * norm.pdf(y, loc=mu, scale=sig)
        exp_pdf = (1 - pi) * expon.pdf(y, scale=lam)
        log_lik = np.sum(np.log(exp_pdf + norm_pdf))
        return -log_lik
    return (TimeReg_neg_log_lik,)


@app.cell
def __(TimeReg_neg_log_lik, datos, minimize):
    initial_guess = [0.7, 2, 10, 3] # x0
    bounds = [(0.001, 0.999), (0, 40), (0, 40), (0, 40)]
    result_TR = minimize(TimeReg_neg_log_lik, x0=initial_guess,
                         args=datos['irt'],
                         bounds=bounds,
                         method='Nelder-Mead',
                         options={'maxiter': 2e10}
                        )
    result_TR
    return bounds, initial_guess, result_TR


@app.cell
def __(datos, expon, norm, np, plt, result_TR):
    pi, lam, mu, sig = result_TR.x
    y = np.linspace(0, 40, 1000)
    norm_pdf = pi * norm.pdf(y, loc=mu, scale=sig)
    exp_pdf = (1 - pi) * expon.pdf(y, scale=lam)
    predicted_mix = exp_pdf + norm_pdf
    plt.hist(datos['irt'], bins=30, density=True);
    plt.plot(y, predicted_mix, color='red')
    plt.axvline(lam, color='black', linestyle=':')
    plt.axvline(mu, color='black', linestyle='--')
    plt.ylim(0, 0.25)
    plt.xlabel('Time (s)')
    plt.ylabel('f(time)')
    plt.show()

    return exp_pdf, lam, mu, norm_pdf, pi, predicted_mix, sig, y


app._unparsable_cell(
    r"""
    %timeit 
    plt.plot(datos)
    """,
    name="__"
)


if __name__ == "__main__":
    app.run()
