import marimo

__generated_with = "0.9.6"
app = marimo.App(width="medium")


@app.cell
def __():
    from scipy.optimize import minimize
    import numpy as np
    # cargar datos breast_cancer
    from sklearn.datasets import load_breast_cancer
    import matplotlib.pyplot as plt
    import pandas as pd
    from scipy.stats import norm
    data = load_breast_cancer()
    # marimo
    return data, load_breast_cancer, minimize, norm, np, pd, plt


@app.cell
def __(data, pd):
    datos = pd.DataFrame(data.data, columns=data.feature_names)
    return (datos,)


@app.cell
def __(datos):
    datos
    return


@app.cell
def __(data):
    x = data.data[:, 0]
    return (x,)


@app.cell
def __(plt, x):
    plt.hist(x, bins=90);
    plt.show()
    return


@app.cell
def __(norm):
    help(norm.pdf)
    return


@app.cell
def __(minimize, norm, np, x):
    def gmm_neg_loglik(params, x):
        mu1, mu2, sig1, sig2, pi_1 = params
        pi_2 = 1 - pi_1
        # joints pdfs
        pdf1 = norm.pdf(x, loc=mu1, scale=sig1)
        pdf2 = norm.pdf(x, loc=mu2, scale=sig2)
        mixture = pi_1 * pdf1 + pi_2 * pdf2
        log_like = np.sum(np.log(mixture))
        return -log_like

    x0 = [10, 15, 3, 5, 0.7]

    bounds = [(0, None), (0, None), (0.1, None), (0.1, None), (0.01, 0.99)]

    result = minimize(
        gmm_neg_loglik, x0, args=x, bounds=bounds
    )

    result
    return bounds, gmm_neg_loglik, result, x0


@app.cell
def __(norm, np, result, x):
    mu1, mu2, sig1, sig2, pi1 = result.x

    x_sim = np.linspace(x.min(), x.max(), 1000)

    pdf1 = pi1 * norm.pdf(x_sim, loc=mu1, scale=sig1)
    pdf2 = (1 - pi1) * norm.pdf(x_sim, loc=mu2, scale=sig2)

    mixture = pdf1 + pdf2
    return mixture, mu1, mu2, pdf1, pdf2, pi1, sig1, sig2, x_sim


@app.cell
def __(data):
    target = data.target
    target
    return (target,)


@app.cell
def __(mixture, pdf1, pdf2, plt, target, x, x_sim):
    plt.hist(x[target==0], bins=30, density=True, alpha=0.5, label='Benign');
    plt.hist(x[target==1], bins=30, density=True, alpha=0.5, label='Malignant');
    plt.plot(x_sim, mixture, color='red', label='Mix')
    plt.plot(x_sim, pdf1, color='black', label='G1')
    plt.plot(x_sim, pdf2, color='blue', label='G2')
    plt.xlabel('Mean radius')
    plt.ylabel('f(x;mu1,mu2,sig1,sig2,pi)')
    plt.legend()
    plt.show()
    return


@app.cell
def __(norm, np):

    # Define the Gaussian + linear function
    def response_rate_model(bins, a, b, t0, c, d):
        """Model the response rate as Gaussian plus linear."""
        gaussian_part = a * np.exp(-((bins - t0)**2) / (2 * b**2))
        linear_part = c * (bins - t0) + d
        return gaussian_part + linear_part

    # Negative log-likelihood function for MLE
    def neg_log_likelihood(params, bins, responses):
        """Negative log-likelihood for the Gaussian + linear model."""
        a, b, t0, c, d = params
        model = response_rate_model(bins, a, b, t0, c, d)

        # Assuming residuals follow a normal distribution (MLE)
        sigma = np.std(responses - model)
        
        # Compute log likelihood (ignoring the constant)
        log_likelihood = np.sum(norm.logpdf(responses, loc=model, scale=sigma))
        
        # Return negative log likelihood for minimization
        return -log_likelihood
    return neg_log_likelihood, response_rate_model


@app.cell
def __(pd, plt):
    data_m326 = pd.read_csv('datasets/m326_respdata.csv')
    plt.scatter(data_m326['bins'], data_m326['resp_norm'])

    return (data_m326,)


@app.cell
def __(data_m326, minimize, neg_log_likelihood):
    initial_guess = [0, 10, 28, 0, 0]
    bins = data_m326['bins']
    responses = data_m326['resp_norm']
    bounds_ = [(0.1, None), (0, None), (0, 180), (0, None), (0, None)]
    result_new = minimize(neg_log_likelihood, 
                          initial_guess, 
                          args=(bins, responses),
                          bounds=bounds_,
                          options={'maxiter': 2e5}
                         )
    result_new
    return bins, bounds_, initial_guess, responses, result_new


@app.cell
def __(a_opt, b_opt, c_opt, d_opt, t0_opt):
    print("Fitted parameters: a =", a_opt, "b =", b_opt, "t0 =", t0_opt, "c =", c_opt, "d =", d_opt)
    return


@app.cell
def __(bins, plt, response_rate_model, responses, result_new):
    a_opt, b_opt, t0_opt, c_opt, d_opt = result_new.x
    # Plot the results
    plt.figure(figsize=(8, 6))

    # Scatterplot of the original data
    plt.scatter(bins, responses, color='blue', label='Normalized Responses', alpha=0.6)

    # Plot the fitted Gaussian + linear model
    fitted_model = response_rate_model(bins, a_opt, b_opt, t0_opt, c_opt, d_opt)
    plt.plot(bins, fitted_model, color='red', label='Fitted Model', lw=2)

    # Add labels and legend
    plt.xlabel('Time Bins')
    plt.ylabel('Normalized Responses')
    plt.title('Fitting Gaussian + Linear Model to Normalized Data')
    plt.legend()

    # Show the plot
    plt.show()
    return a_opt, b_opt, c_opt, d_opt, fitted_model, t0_opt


@app.cell
def __(fitted_model, plt, responses):
    error = responses - fitted_model
    plt.scatter(responses, error)
    return (error,)


if __name__ == "__main__":
    app.run()
