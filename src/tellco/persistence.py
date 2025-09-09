import pandas as pd
import joblib
import mysql.connector

def save_model(model, path: str):
    """Save model to disk."""
    joblib.dump(model, path)

def load_model(path: str):
    """Load model from disk."""
    return joblib.load(path)

def export_to_mysql(df: pd.DataFrame, table_name: str, db_config: dict):
    """Export DataFrame to MySQL table."""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create table if not exists
    cols = ', '.join([f"`{col}` TEXT" for col in df.columns])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")

    # Insert data row by row
    for _, row in df.iterrows():
        placeholders = ', '.join(['%s'] * len(row))
        sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(sql, tuple(map(str, row.values)))

    conn.commit()
    cursor.close()
    conn.close()
