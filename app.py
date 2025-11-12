import streamlit as st
import pandas as pd

#uv run streamlit run app.py
df = pd.read_csv("covid_death_demographics.csv")
df_st = st.dataframe(df)


st.title("Covid Death Demographics EDA")
st.subheader("Determining susceptability of young people to covid by demographic groups")

st.write(df)





