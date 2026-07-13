import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(df: pd.DataFrame, target_col: str = 'quality'):
    """Handle duplicates, missing values, scaling, and feature engineering."""
    df = df.drop_duplicates().reset_index(drop=True)
    
    # Feature engineering
    df['alcohol_vol_acidity_ratio'] = df['alcohol'] / (df['volatile acidity'] + 1e-5)
    
    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    return X_scaled, y, scaler
