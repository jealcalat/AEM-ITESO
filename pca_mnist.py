import marimo

__generated_with = "0.9.6"
app = marimo.App(width="medium")


@app.cell
def __():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA
    from sklearn.datasets import fetch_openml
    from sklearn.preprocessing import StandardScaler
    import sys
    # Load the MNIST dataset
    print("Loading MNIST dataset...")
    mnist = fetch_openml('mnist_784', version=1)
    X, y = mnist["data"], mnist["target"]

    # Normalize the pixel values
    X = X / 255.0

    # Apply PCA
    pca = PCA(n_components=0.95)  # Keep 95% of variance
    X_reduced = pca.fit_transform(X)
    print(f"Original shape: {X.shape}, Reduced shape: {X_reduced.shape}")

    # Inverse transform (Reconstruction)
    X_reconstructed = pca.inverse_transform(X_reduced)

    # Plot images
    def plot_images(original, reconstructed, n_images=10):
        plt.figure(figsize=(15, 5))
        for i in range(n_images):
            # Original image
            plt.subplot(2, n_images, i + 1)
            plt.imshow(original.iloc[i].values.reshape(28, 28), cmap='binary')  # Use `.iloc`
            plt.axis('off')
            if i == 0:
                plt.title("Original", fontsize=12)
            
            # Reconstructed image
            plt.subplot(2, n_images, i + 1 + n_images)
            plt.imshow(reconstructed[i].reshape(28, 28), cmap='binary')
            plt.axis('off')
            if i == 0:
                plt.title("Reconstructed", fontsize=12)

        plt.show()

    # Plot original and reconstructed images
    plot_images(X, X_reconstructed)

    return (
        PCA,
        StandardScaler,
        X,
        X_reconstructed,
        X_reduced,
        fetch_openml,
        mnist,
        np,
        pca,
        plot_images,
        plt,
        sys,
        y,
    )


@app.cell
def __(X):
    X.shape
    return


if __name__ == "__main__":
    app.run()
