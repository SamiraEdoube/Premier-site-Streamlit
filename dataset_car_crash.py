import ssl
import streamlit as st
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/car_crashes.csv"
df = pd.read_csv(url)

st.title("Scatter plot avec Streamlit")

x_col = "speeding"
y_col = "alcohol"

st.write(f"Scatter plot entre {x_col} et {y_col}")
st.scatter_chart(df[[x_col, y_col]])
