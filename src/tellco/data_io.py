import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Loads telecom dataset from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the dataset by replacing missing numerical values with the mean."""
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Optionally drop rows with missing categorical values (or fill with 'Unknown')
    categorical_cols = df.select_dtypes(include='object').columns
    df[categorical_cols] = df[categorical_cols].fillna('Unknown')

    return df
