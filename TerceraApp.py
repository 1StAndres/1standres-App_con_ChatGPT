# El siguiente codigo fue realizado usando chatGPT
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Inicializar las sesiones para almacenar datos (se puede mejorar con una base de datos en producción)
if 'ingresos' not in st.session_state:
    st.session_state.ingresos = []
if 'gastos' not in st.session_state:
    st.session_state.gastos = []
if 'presupuesto' not in st.session_state:
    st.session_state.presupuesto = 0.0
if 'metas_ahorro' not in st.session_state:
    st.session_state.metas_ahorro = {}

# Función para registrar ingresos
def registrar_ingreso(monto, categoria, fecha):
    st.session_state.ingresos.append({
        'monto': monto,
        'categoria': categoria,
        'fecha': fecha
    })

# Función para registrar gastos
def registrar_gasto(monto, categoria, fecha):
    st.session_state.gastos.append({
        'monto': monto,
        'categoria': categoria,
        'fecha': fecha
    })

# Función para registrar presupuesto
def establecer_presupuesto(presupuesto):
    st.session_state.presupuesto = presupuesto

# Función para establecer metas de ahorro
def establecer_meta_ahorro(meta, categoria):
    st.session_state.metas_ahorro[categoria] = meta

# Función para calcular el total de ingresos y gastos
def calcular_totales():
    ingresos_totales = sum(ingreso['monto'] for ingreso in st.session_state.ingresos)
    gastos_totales = sum(gasto['monto'] for gasto in st.session_state.gastos)
    return ingresos_totales, gastos_totales

# Función para generar reporte semanal y mensual
def generar_reporte():
    ingresos_totales, gastos_totales = calcular_totales()

    # Reporte mensual
    reporte_mensual = {
        'Presupuesto': st.session_state.presupuesto,
        'Ingresos Totales': ingresos_totales,
        'Gastos Totales': gastos_totales,
        'Diferencia (Ingreso - Gasto)': ingresos_totales - gastos_totales,
        'Meta de Ahorro': sum(st.session_state.metas_ahorro.values()),
        'Diferencia con Meta de Ahorro': sum(st.session_state.metas_ahorro.values()) - (st.session_state.presupuesto - gastos_totales)
    }

    # Reporte semanal (last 7 days)
    fecha_hoy = datetime.today()
    fecha_semana_pasada = fecha_hoy - timedelta(days=7)
    
    ingresos_semanales = sum(ingreso['monto'] for ingreso in st.session_state.ingresos if ingreso['fecha'] >= fecha_semana_pasada)
    gastos_semanales = sum(gasto['monto'] for gasto in st.session_state.gastos if gasto['fecha'] >= fecha_semana_pasada)
    
    reporte_semanal = {
        'Ingresos Semanales': ingresos_semanales,
        'Gastos Semanales': gastos_semanales,
        'Diferencia Semanal (Ingreso - Gasto)': ingresos_semanales - gastos_semanales,
    }

    return reporte_mensual, reporte_semanal

# Título y descripción
st.title('Registro de Finanzas Personales')
st.write('Registra tus ingresos, gastos, presupuesto y metas de ahorro. Genera reportes semanales y mensuales.')

# Ingresar presupuesto mensual
presupuesto = st.number_input('Establecer presupuesto mensual:', min_value=0.0, value=st.session_state.presupuesto)
if presupuesto != st.session_state.presupuesto:
    establecer_presupuesto(presupuesto)

# Ingresar ingresos
st.subheader('Registrar Ingreso')
monto_ingreso = st.number_input('Monto del ingreso:', min_value=0.0)
categoria_ingreso = st.text_input('Categoría del ingreso (Ej: Salario, Freelance, etc.)')
fecha_ingreso = st.date_input('Fecha del ingreso:', datetime.today())

if st.button('Registrar Ingreso'):
    registrar_ingreso(monto_ingreso, categoria_ingreso, fecha_ingreso)
    st.success('Ingreso registrado con éxito')

# Ingresar gastos
st.subheader('Registrar Gasto')
monto_gasto = st.number_input('Monto del gasto:', min_value=0.0)
categoria_gasto = st.text_input('Categoría del gasto (Ej: Renta, Alimentación, etc.)')
fecha_gasto = st.date_input('Fecha del gasto:', datetime.today())

if st.button('Registrar Gasto'):
    registrar_gasto(monto_gasto, categoria_gasto, fecha_gasto)
    st.success('Gasto registrado con éxito')

# Establecer metas de ahorro
st.subheader('Establecer Metas de Ahorro')
categoria_meta = st.text_input('Categoría de meta de ahorro (Ej: Emergencias, Vacaciones, etc.)')
monto_meta = st.number_input('Monto objetivo de ahorro para la categoría:', min_value=0.0)

if st.button('Establecer Meta de Ahorro'):
    establecer_meta_ahorro(monto_meta, categoria_meta)
    st.success('Meta de ahorro registrada con éxito')

# Mostrar reporte
st.subheader('Reportes Financieros')

reporte_mensual, reporte_semanal = generar_reporte()

# Reporte mensual
st.write('### Reporte Mensual')
st.write(f"Presupuesto mensual: ${reporte_mensual['Presupuesto']}")
st.write(f"Ingresos totales: ${reporte_mensual['Ingresos Totales']}")
st.write(f"Gastos totales: ${reporte_mensual['Gastos Totales']}")
st.write(f"Diferencia (Ingreso - Gasto): ${reporte_mensual['Diferencia (Ingreso - Gasto)']}")
st.write(f"Meta de ahorro: ${reporte_mensual['Meta de Ahorro']}")
st.write(f"Diferencia con meta de ahorro: ${reporte_mensual['Diferencia con Meta de Ahorro']}")

# Reporte semanal
st.write('### Reporte Semanal')
st.write(f"Ingresos semanales: ${reporte_semanal['Ingresos Semanales']}")
st.write(f"Gastos semanales: ${reporte_semanal['Gastos Semanales']}")
st.write(f"Diferencia semanal (Ingreso - Gasto): ${reporte_semanal['Diferencia Semanal (Ingreso - Gasto)']}")

