# El siguiente codigo fue realizado usando chatGPT
import streamlit as st

# Título de la app
st.title('Mi primera app')

# Información sobre el autor
st.write('Esta app fue elaborada por Andres Arbelaez Morales.')

# Solicitar el nombre del usuario
nombre_usuario = st.text_input('¿Cómo te llamas?')

# Si el usuario ha ingresado un nombre, mostrar un mensaje de bienvenida
if nombre_usuario:
    st.write(f'{nombre_usuario}, te doy la bienvenida a mi primera app.')
