import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Inicializar los registros de gatitos y adopciones si no existen en la sesión
if 'gatitos' not in st.session_state:
    st.session_state.gatitos = []

if 'gatitos_adoptados' not in st.session_state:
    st.session_state.gatitos_adoptados = []

# Función para agregar un gatito
def agregar_gatito(nombre, edad, peso, enfermedades):
    st.session_state.gatitos.append({
        'nombre': nombre,
        'edad': edad,
        'peso': peso,
        'enfermedades': enfermedades
    })

# Función para registrar una adopción
def registrar_adopcion(nombre_gatito, nombre_dueño, direccion_dueño):
    # Encontrar el gatito que ha sido adoptado
    gatito = next((g for g in st.session_state.gatitos if g['nombre'] == nombre_gatito), None)
    
    if gatito:
        # Mover el gatito al registro de adoptados
        st.session_state.gatitos_adoptados.append({
            **gatito,  # Copiar los datos del gatito
            'nombre_dueño': nombre_dueño,
            'direccion_dueño': direccion_dueño,
            'fecha_adopcion': datetime.today()
        })
        # Eliminar el gatito del registro de gatitos disponibles
        st.session_state.gatitos.remove(gatito)

# Título de la app
st.title("Registro del Refugio de Gatitos")

# Sección de registro de nuevos gatitos
st.subheader("Registrar Nuevo Gatito")

# Campos para ingresar los datos del gatito
nombre_gatito = st.text_input("Nombre del Gatito")
edad_gatito = st.number_input("Edad (en meses)", min_value=0, step=1)
peso_gatito = st.number_input("Peso (en kg)", min_value=0.0, step=0.1)
enfermedades_gatito = st.text_area("Enfermedades o condiciones médicas")

# Validaciones para los gatitos
if edad_gatito < 0:
    st.warning("La edad debe ser un número positivo.")
if peso_gatito <= 0:
    st.warning("El peso debe ser un número mayor a 0.")

# Botón para agregar el gatito al registro
if st.button("Agregar Gatito"):
    if nombre_gatito and edad_gatito > 0 and peso_gatito > 0:
        agregar_gatito(nombre_gatito, edad_gatito, peso_gatito, enfermedades_gatito)
        st.success(f"Gatito '{nombre_gatito}' agregado con éxito!")
    else:
        st.warning("Por favor, complete todos los campos correctamente.")

# Mostrar los gatitos disponibles para adopción
st.subheader("Gatitos Disponibles para Adopción")
if st.session_state.gatitos:
    gatitos_df = pd.DataFrame(st.session_state.gatitos)
    st.write(gatitos_df)
else:
    st.write("No hay gatitos disponibles para adopción.")

# Sección de adopciones
st.subheader("Registrar Adopción de Gatito")

# Seleccionar un gatito disponible para adopción
nombre_gatito_adopcion = st.selectbox("Selecciona el gatito a adoptar", [g['nombre'] for g in st.session_state.gatitos])

# Ingresar los datos del adoptante
nombre_dueño = st.text_input("Nombre del Dueño")
direccion_dueño = st.text_area("Dirección del Dueño")

# Validaciones para los adoptantes
if not nombre_dueño:
    st.warning("El nombre del dueño no puede estar vacío.")
if not direccion_dueño:
    st.warning("La dirección del dueño no puede estar vacía.")

# Botón para registrar la adopción
if st.button("Registrar Adopción"):
    if nombre_dueño and direccion_dueño:
        registrar_adopcion(nombre_gatito_adopcion, nombre_dueño, direccion_dueño)
        st.success(f"El gatito '{nombre_gatito_adopcion}' ha sido adoptado con éxito!")
    else:
        st.warning("Por favor, complete los datos del adoptante correctamente.")

# Mostrar los gatitos adoptados
st.subheader("Gatitos Adoptados")
if st.session_state.gatitos_adoptados:
    adoptados_df = pd.DataFrame(st.session_state.gatitos_adoptados)
    st.write(adoptados_df)
else:
    st.write("No hay gatitos adoptados aún.")

# **Gráficos** de estadísticas

# Gráfico de adopciones por mes
if st.session_state.gatitos_adoptados:
    # Asegúrate de que la columna 'fecha_adopcion' sea tipo datetime
    fechas_adopcion = [g['fecha_adopcion'] for g in st.session_state.gatitos_adoptados]
    
    # Convertir las fechas a tipo datetime (si no lo son ya)
    fechas_adopcion = pd.to_datetime(fechas_adopcion)
    
    # Extraer el mes (y el año) de la fecha de adopción
    meses_adopcion = fechas_adopcion.dt.to_period('M').dt.to_timestamp()  # Convertir a periodo mensual
    
    # Convertir en DataFrame para la agrupación
    df_adopciones = pd.DataFrame({'fecha_adopcion': meses_adopcion})
    
    # Agrupar por mes y contar el número de adopciones por mes
    adopciones_por_mes = df_adopciones.groupby('fecha_adopcion').size().reset_index(name='cantidad')
    
    st.subheader("Gráfico: Adopciones por Mes")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=adopciones_por_mes, x='fecha_adopcion', y='cantidad', ax=ax)
    
    # Formatear las etiquetas del eje X para que se muestren el mes y año
    ax.set_xticklabels(adopciones_por_mes['fecha_adopcion'].dt.strftime('%b %Y'), rotation=45)
    ax.set_xlabel('Mes')
    ax.set_ylabel('Número de Adopciones')
    st.pyplot(fig)



# Gráfico de distribución de edades
if st.session_state.gatitos:
    edades = [g['edad'] for g in st.session_state.gatitos]
    st.subheader("Gráfico: Distribución de Edades de los Gatitos Disponibles")
    fig, ax = plt.subplots()
    sns.histplot(edades, kde=True, ax=ax, color='skyblue')
    ax.set_xlabel('Edad (en meses)')
    ax.set_ylabel('Número de Gatitos')
    st.pyplot(fig)

# Gráfico de distribución de pesos
if st.session_state.gatitos:
    pesos = [g['peso'] for g in st.session_state.gatitos]
    st.subheader("Gráfico: Distribución de Pesos de los Gatitos Disponibles")
    fig, ax = plt.subplots()
    sns.histplot(pesos, kde=True, ax=ax, color='lightgreen')
    ax.set_xlabel('Peso (en kg)')
    ax.set_ylabel('Número de Gatitos')
    st.pyplot(fig)
