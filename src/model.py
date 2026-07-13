from pyod.models.abod import ABOD

def train_abod(X, n_neighbors=10, contamination=0.05, method='fast', random_state=42):
    """Train and return a fitted ABOD model."""
    model = ABOD(
        method=method,
        n_neighbors=n_neighbors,
        contamination=contamination,
        random_state=random_state
    )
    model.fit(X)
    return model
