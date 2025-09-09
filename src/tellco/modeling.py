import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics.pairwise import euclidean_distances

def normalize_df(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Normalize selected columns."""
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled

def run_kmeans(df: pd.DataFrame, columns: list, k: int = 3) -> pd.DataFrame:
    """Run KMeans and add cluster labels."""
    model = KMeans(n_clusters=k, random_state=42)
    df_clustered = df.copy()
    df_clustered['cluster'] = model.fit_predict(df[columns])
    return df_clustered, model

def run_pca(df: pd.DataFrame, columns: list, n_components: int = 2) -> pd.DataFrame:
    """Perform PCA for dimensionality reduction."""
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df[columns])
    for i in range(n_components):
        df[f'pca_{i+1}'] = components[:, i]
    return df, pca

def calculate_euclidean_scores(df: pd.DataFrame, features: list, cluster_centers, cluster_labels, target_cluster: int) -> pd.Series:
    """Calculate Euclidean distance from a specific cluster center."""
    distances = euclidean_distances(df[features], [cluster_centers[target_cluster]])
    return pd.Series(distances.flatten(), index=df.index)

def train_regression_model(X: pd.DataFrame, y: pd.Series) -> LinearRegression:
    """Train linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    return model
