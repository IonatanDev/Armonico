import streamlit as st

st.title('Resolucion numerica del oscilador armonico')

st.title('Medimos las constantes fisicas de los objetos')
#Definimos algunas constantes
m = st.number_input('Masa (Kg):', value=1.0)
k = st.number_input('Constante del resorte (N/m):', value=1.0)
l_0 = st.number_input('Longitud natural del resorte (m):', value=1.0)

st.title('Determinamos las condiciones iniciales')
#Establecemos condiciones iniciales
x_0 = st.numeer_input('Posicion inicial (m):')
v_0 = st.number_input('Velocidad inicial (m/s):')
a_0 = -k*(x_0-l_0)/m

st.title('Definimos el algoritmo recursivo')
st.latex(r''' x_i = x_{i-1} + v_{i-1} \cdot \Delta t''')
st.latex(r''' v_i = v_{i-1} + a_{i-1} \cdot \Delta t''')
st.latex(r''' a_i = \frac{-k \cdot (l_0 - x_i)}{m}''')


