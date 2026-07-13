import pandas as pd

def load_wine_data(filepath: str, sep: str = ';') -> pd.DataFrame:
    """Load and return the wine dataset."""
    return pd.read_csv(filepath, sep=sep)
