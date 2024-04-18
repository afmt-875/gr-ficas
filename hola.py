import streamlit as st
import pandas as pd
#creamos título de la App
st.title("Titanic App")
st.header("Titanic Graphs - App")
st.write("Gráficas del dataset Titanic")

titanic_link = 'titanic 2.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)