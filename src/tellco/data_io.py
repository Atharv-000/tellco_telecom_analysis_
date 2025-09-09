import pandas as pd

# Define the load_data and clean_data functions
def load_data(filepath: str) -> pd.DataFrame:
    """Loads telecom dataset from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the dataset by replacing missing numerical values with the mean."""
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    categorical_cols = df.select_dtypes(include='object').columns
    df[categorical_cols] = df[categorical_cols].fillna('Unknown')

    return df

# Reload the dataset
data_path = "D:\JupyterWork\Github\telcom_data (2).xlsx - Sheet1.csv"
df_raw = load_data(data_path)
df_clean = clean_data(df_raw)

# Show shape and head of cleaned dataset
df_clean.shape, df_clean.head()
