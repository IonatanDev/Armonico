import streamlit as st

st.title('Resolucion numerica del oscilador armonico')

#Definimos algunas constantes
m = st.slider('Masa (Kg):')
k = st.slider('Constante del resorte (N/m):')
l_0 = st.slider('Longitud natural del resorte (m):')

#Establecemos condiciones iniciales

