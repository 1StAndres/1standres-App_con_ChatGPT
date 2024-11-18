# El siguiente codigo fue realizado usando chatGPT

import streamlit as st
import pandas as pd

# Inicializar el registro de materias
if 'materias' not in st.session_state:
    st.session_state.materias = []

# Función para agregar materia
def agregar_materia(nombre, calificacion, creditos, tipologia):
    st.session_state.materias.append({
        'nombre': nombre,
        'calificacion': calificacion,
        'creditos': creditos,
        'tipologia': tipologia
    })

# Función para calcular el PAPA global
def calcular_papa_global():
    total_creditos = sum(materia['creditos'] for materia in st.session_state.materias)
    ponderado_acumulado = sum(materia['calificacion'] * materia['creditos'] for materia in st.session_state.materias)
    if total_creditos > 0:
        return ponderado_acumulado / total_creditos
    else:
        return 0.0

# Función para calcular el PAPA por tipología
def calcular_papa_por_tipologia(tipologia):
    materias_filtradas = [materia for materia in st.session_state.materias if materia['tipologia'] == tipologia]
    total_creditos = sum(materia['creditos'] for materia in materias_filtradas)
    ponderado_acumulado = sum(materia['calificacion'] * materia['creditos'] for materia in materias_filtradas)
    if total_creditos > 0:
        return ponderado_acumulado / total_creditos
    else:
        return 0.0

# Título de la app
st.title("Cálculo del Promedio Académico Ponderado Acumulado (PAPA)")

# Ingreso de datos de materia
st.subheader("Registrar Materia")

# Campos para ingresar la materia
nombre = st.text_input("Nombre de la materia")
calificacion = st.number_input("Calificación obtenida (0-5)", min_value=0.0, max_value=5.0, step=0.1)
creditos = st.number_input("Créditos de la materia", min_value=1, step=1)
tipologia = st.selectbox("Tipología de la asignatura", ["Teórica", "Práctica", "Electiva"])

# Botón para agregar la materia
if st.button("Agregar Materia"):
    if nombre and calificacion and creditos and tipologia:
        agregar_materia(nombre, calificacion, creditos, tipologia)
        st.success(f"Materia '{nombre}' agregada con éxito!")
    else:
        st.warning("Por favor, complete todos los campos.")

# Mostrar las materias registradas
st.subheader("Materias Registradas")
if st.session_state.materias:
    materias_df = pd.DataFrame(st.session_state.materias)
    st.write(materias_df)
else:
    st.write("Aún no se han registrado materias.")

# Cálculo del PAPA global
st.subheader("Cálculo del PAPA Global")
if st.session_state.materias:
    papa_global = calcular_papa_global()
    st.write(f"El PAPA Global es: {papa_global:.2f}")
else:
    st.write("No se pueden calcular los promedios, no hay materias registradas.")

# Cálculo del PAPA por tipología
st.subheader("Cálculo del PAPA por Tipología")
tipologias = ["Teórica", "Práctica", "Electiva"]
tipologia_seleccionada = st.selectbox("Selecciona la tipología para calcular el PAPA", tipologias)

if st.session_state.materias:
    papa_por_tipologia = calcular_papa_por_tipologia(tipologia_seleccionada)
    st.write(f"El PAPA para las asignaturas '{tipologia_seleccionada}' es: {papa_por_tipologia:.2f}")
else:
    st.write("No se pueden calcular los promedios, no hay materias registradas.")
