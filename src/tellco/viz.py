import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_handsets(df: pd.DataFrame, top_n: int = 10):
    """Plot top N handsets used."""
    top_handsets = df['Handset Type'].value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_handsets.values, y=top_handsets.index)
    plt.title(f'Top {top_n} Handsets')
    plt.xlabel('Count')
    plt.ylabel('Handset Type')
    plt.tight_layout()
    plt.show()

def plot_top_manufacturers(df: pd.DataFrame, top_n: int = 3):
    """Plot top N handset manufacturers."""
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(top_n)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top_manufacturers.values, y=top_manufacturers.index)
    plt.title(f'Top {top_n} Handset Manufacturers')
    plt.xlabel('Count')
    plt.ylabel('Manufacturer')
    plt.tight_layout()
    plt.show()

def plot_top_handsets_per_manufacturer(df: pd.DataFrame, top_n_manufacturers=3, top_n_handsets=5):
    """Plot top handsets per top manufacturers."""
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(top_n_manufacturers).index
    df_filtered = df[df['Handset Manufacturer'].isin(top_manufacturers)]
    
    plt.figure(figsize=(12, 6))
    for i, manu in enumerate(top_manufacturers, 1):
        plt.subplot(1, top_n_manufacturers, i)
        subset = df_filtered[df_filtered['Handset Manufacturer'] == manu]
        top_handsets = subset['Handset Type'].value_counts().head(top_n_handsets)
        sns.barplot(y=top_handsets.index, x=top_handsets.values)
        plt.title(manu)
        plt.xlabel('Count')
        plt.ylabel('')
    
    plt.tight_layout()
    plt.show()
