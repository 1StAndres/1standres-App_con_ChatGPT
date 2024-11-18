import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Si ya tienes los registros en `st.session_state.gatitos_adoptados`, usaremos esa variable.
# Ejemplo de cómo pueden estar estructurados los datos de los gatitos (si no tienes datos previos, puedes definir algunos aquí):
# st.session_state.gatitos_adoptados = [
#     {'nombre': 'Gatito1', 'peso': 2.5, 'fecha_adopcion': '2023-06-15'},
#     {'nombre': 'Gatito2', 'peso': 3.0, 'fecha_adopcion': '2023-06-17'},
#     {'nombre': 'Gatito3', 'peso': 4.0, 'fecha_adopcion': '2023-07-01'},
#     {'nombre': 'Gatito4', 'peso': 2.3, 'fecha_adopcion': '2023-07-05'},
# ]

# Asegúrate de tener gatitos adoptados en el estado de sesión antes de ejecutar el gráfico
if st.session_state.gatitos_adoptados:
    # Extraer los datos necesarios de los gatitos adoptados
    fechas_adopcion = [g['fecha_adopcion'] for g in st.session_state.gatitos_adoptados]
    nombres = [g['nombre'] for g in st.session_state.gatitos_adoptados]
    pesos = [g['peso'] for g in st.session_state.gatitos_adoptados]
    
    # Convertir las fechas a tipo datetime (si no lo son ya)
    fechas_adopcion = pd.to_datetime(fechas_adopcion)
    
    # Extraer el mes y año (en formato 'YYYY-MM') para el agrupamiento
    meses_adopcion = fechas_adopcion.dt.to_period('M').astype(str)  # Convertir a formato 'YYYY-MM'
    
    # Crear un DataFrame con los datos
    df_adopciones = pd.DataFrame({
        'fecha_adopcion': meses_adopcion,
        'nombre': nombres,
        'peso': pesos
    })
    
    # Agrupar por mes y contar las adopciones por mes
    adopciones_por_mes = df_adopciones.groupby('fecha_adopcion').size().reset_index(name='cantidad')
    
    # Crear el gráfico de barras
    st.subheader("Gráfico: Adopciones por Mes")
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Dibujar las barras
    sns.barplot(data=adopciones_por_mes, x='fecha_adopcion', y='cantidad', ax=ax, color='lightblue')
    
    # Añadir los nombres y pesos como etiquetas en las barras
    for idx, row in adopciones_por_mes.iterrows():
        mes = row['fecha_adopcion']
        cantidad = row['cantidad']
        
        # Obtener los gatitos de ese mes
        gatitos_del_mes = df_adopciones[df_adopciones['fecha_adopcion'] == mes]
        
        # Colocar el nombre y peso sobre la barra para cada gatito adoptado en ese mes
        for i, gatito in gatitos_del_mes.iterrows():
            nombre = gatito['nombre']
            peso = gatito['peso']
            
            # Añadir el nombre y peso en la barra correspondiente
            ax.text(
                mes, cantidad + 0.1, f"{nombre}\n{peso}kg", 
                ha='center', va='bottom', fontsize=10
            )
    
    # Configuración de las etiquetas del eje X
    ax.set_xticklabels(adopciones_por_mes['fecha_adopcion'], rotation=45)
    ax.set_xlabel('Mes')
    ax.set_ylabel('Número de Adopciones')
    ax.set_title('Número de Adopciones por Mes con Nombres y Pesos de Gatitos')
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

