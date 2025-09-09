import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tellco.data_io import load_data, clean_data
from tellco.features import add_total_data, aggregate_user_overview
from tellco.viz import plot_top_handsets, plot_top_manufacturers, plot_top_handsets_per_manufacturer

st.set_page_config(page_title="TellCo Dashboard", layout="wide")
st.title("📱 TellCo Telecom Analytics Dashboard")

# Load data
@st.cache_data
def load_and_prepare():
    df = load_data("data/telcom_data.csv")
    df = clean_data(df)
    df = add_total_data(df)
    return df

df = load_and_prepare()

st.sidebar.header("Choose Analysis")
section = st.sidebar.radio("Go to", ["Top Handsets", "Top Manufacturers", "Top Handsets per Manufacturer"])

if section == "Top Handsets":
    st.subheader("Top 10 Handsets")
    plot_top_handsets(df)

elif section == "Top Manufacturers":
    st.subheader("Top 3 Handset Manufacturers")
    plot_top_manufacturers(df)

elif section == "Top Handsets per Manufacturer":
    st.subheader("Top 5 Handsets per Top 3 Manufacturers")
    plot_top_handsets_per_manufacturer(df)
