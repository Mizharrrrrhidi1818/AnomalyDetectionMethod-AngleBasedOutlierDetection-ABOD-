import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_pca_outliers(X_scaled, labels, scores, title="PCA: Outliers vs Inliers"):
    """Generate PCA scatter plot highlighting outliers."""
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    
    plt.figure(figsize=(10, 7))
    plt.scatter(X_pca[labels==0, 0], X_pca[labels==0, 1], 
                c='steelblue', s=20, alpha=0.6, label='Inliers')
    plt.scatter(X_pca[labels==1, 0], X_pca[labels==1, 1], 
                c='crimson', s=50, alpha=0.9, label='Outliers', edgecolors='black')
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
