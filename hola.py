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
ax.hist(titanic_data['Fare'])
st.header("Histograma del Titanic")
st.pyplot(fig)

st.markdown("____")

fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Pclass')
ax2.set_ylabel('Fare')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)