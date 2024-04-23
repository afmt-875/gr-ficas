import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

st.markdown("____")

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data['Age'], titanic_data['Fare'])
ax3.set_ylabel('Edad')
ax3.set_ylabel('Tarifa')
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)

st.markdown("____")

fig4, ax4 = plt.subplots()
ax4 = titanic_data.boxplot(['Age'])
ax4.set_ylabel('Edad')
st.header("Grafica de Cajas por Edad")
st.pyplot(fig4)

st.markdown("____")

fig5,ax5 = plt.subplots()
hist_class = np.histogram(titanic_data['Pclass'], bins = 3, range = (1,3))[0]

labels = ['1','2','3']
colors = ['tab:blue', 'tab:red', 'tab:green']
explode = [0,0,0.2]

ax5.pie(hist_class,
        labels = labels,
         colors = colors, 
         autopct  = '%.0f%%',
         explode = explode, 
         shadow = True)
st.header("Grafica de Pastel - Clase Social")
st.pyplot(fig5)
st.dataframe(hist_class)