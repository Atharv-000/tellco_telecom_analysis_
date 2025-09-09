from tellco.data_io import load_data, clean_data
from tellco.features import add_total_data, aggregate_engagement_metrics
from tellco.modeling import normalize_df, run_kmeans

# Load & prepare data
df = load_data("data/telcom_data.csv")
df = clean_data(df)
df = add_total_data(df)

# Aggregate engagement features
engagement_df = aggregate_engagement_metrics(df)

# Normalize and cluster
features = ['session_count', 'total_session_duration', 'total_traffic']
engagement_df_norm = normalize_df(engagement_df, features)
engagement_clustered, model = run_kmeans(engagement_df_norm, features, k=3)

# Print result
print(engagement_clustered.head())
