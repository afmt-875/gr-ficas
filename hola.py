import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#creamos título de la App
st.title("Titanic App")
st.header("Antonio Millán - A01704728")
st.write("Gráficas del dataset Titanic")

titanic_link = 'titanic 2.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)