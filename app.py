import streamlit as st
import pandas as pd

#uv run streamlit run app.py

st.title("Covid Death Demographics EDA")

df = pd.read_csv("covid_death_demographics.csv")
st.write(df)




