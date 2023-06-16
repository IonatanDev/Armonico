import streamlit as st

st.title('Resolucion numerica del oscilador armonico')

#Definimos algunas constantes
m = st.slider('Masa (Kg):', value=1.0)
k = st.slider('Constante del resorte (N/m):', value=1.0)
l_0 = st.slider('Longitud natural del resorte (m):', value=1.0)

#Establecemos condiciones iniciales

