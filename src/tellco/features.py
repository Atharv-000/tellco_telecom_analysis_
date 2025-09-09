import pandas as pd

def add_total_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add total data column (DL + UL) per row."""
    df['Total Data (Bytes)'] = df['Total UL (Bytes)'] + df['Total DL (Bytes)']
    return df

def aggregate_user_overview(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate user-level overview features."""
    agg_df = df.groupby('MSISDN/Number').agg(
        session_count=('Bearer Id', 'count'),
        total_session_duration=('Dur. (ms)', 'sum'),
        total_dl=('Total DL (Bytes)', 'sum'),
        total_ul=('Total UL (Bytes)', 'sum'),
    ).reset_index()
    
    agg_df['total_data'] = agg_df['total_dl'] + agg_df['total_ul']
    
    return agg_df

def aggregate_app_usage_per_user(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total app usage data per user."""
    app_cols = [
        'Social Media DL (Bytes)', 'Social Media UL (Bytes)',
        'Google DL (Bytes)', 'Google UL (Bytes)',
        'Email DL (Bytes)', 'Email UL (Bytes)',
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)',
        'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
        'Gaming DL (Bytes)', 'Gaming UL (Bytes)',
        'Other DL (Bytes)', 'Other UL (Bytes)',
    ]
    
    user_app_df = df.groupby('MSISDN/Number')[app_cols].sum().reset_index()
    
    # Combine DL + UL per app
    for app in ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']:
        user_app_df[f'{app} Total (Bytes)'] = (
            user_app_df[f'{app} DL (Bytes)'] + user_app_df[f'{app} UL (Bytes)']
        )
    
    return user_app_df
