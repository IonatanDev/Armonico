import streamlit as st
import matplotlib.pyplot as plt

st.title('Resolucion numerica del oscilador armonico')

st.title('Medimos las constantes fisicas de los objetos')
#Definimos algunas constantes
m = st.number_input('Masa (Kg):', value=1.0)
k = st.number_input('Constante del resorte (N/m):', value=1.0)
l_0 = st.number_input('Longitud natural del resorte (m):', value=1.0)

st.title('Determinamos las condiciones iniciales')
#Establecemos condiciones iniciales
x_0 = st.number_input('Posicion inicial (m):')
v_0 = st.number_input('Velocidad inicial (m/s):')
a_0 = -k*(x_0-l_0)/m

st.title('Definimos el algoritmo recursivo')
st.latex(r''' x_i = x_{i-1} + v_{i-1} \cdot \Delta t''')
st.latex(r''' v_i = v_{i-1} + a_{i-1} \cdot \Delta t''')
st.latex(r''' a_i = \frac{-k \cdot (x_i - l_0)}{m}''')

st.title('Definimos el paso y el numero de iteraciones')

delta = st.number_input('largo temporal del paso (s):', value=0.1, step = 0.001)
N = st.slider('Numero de iteraciones:', value = 1000)

st.title('Ejecutamos la simulacion y graficamos los resultados')

X = [x_0]
V = [v_0]
A = [a_0]
t = [0]

for i in range (1,N+1):
    X.append(X[i-1] + V[i-1] * delta)
    V.append(V[i-1] + A[i-1] * delta)
    A.append(-k * (X[i]- l_0) / m)
    t.append(t[i-1] + delta)

fig, ax = plt.subplots()
ax.plot(t, X)
st.pyplot(fig)

st.write('Valores de x')
st.write(X)
st.write('Valores de v')
st.write(V)
st.write('Valores de a')
st.write(A)

