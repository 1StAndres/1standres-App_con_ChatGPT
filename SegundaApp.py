#El siguiente codigo fue realizado con chatGPT
import streamlit as st

# Función para realizar las conversiones
def convertir(valor, categoria, conversion):
    if categoria == "Temperatura":
        if conversion == "Celsius a Fahrenheit":
            return (valor * 9/5) + 32
        elif conversion == "Fahrenheit a Celsius":
            return (valor - 32) * 5/9
        elif conversion == "Celsius a Kelvin":
            return valor + 273.15
        elif conversion == "Kelvin a Celsius":
            return valor - 273.15
    elif categoria == "Longitud":
        if conversion == "Pies a metros":
            return valor * 0.3048
        elif conversion == "Metros a pies":
            return valor / 0.3048
        elif conversion == "Pulgadas a centímetros":
            return valor * 2.54
        elif conversion == "Centímetros a pulgadas":
            return valor / 2.54
    elif categoria == "Peso/Masa":
        if conversion == "Libras a kilogramos":
            return valor * 0.453592
        elif conversion == "Kilogramos a libras":
            return valor / 0.453592
        elif conversion == "Onzas a gramos":
            return valor * 28.3495
        elif conversion == "Gramos a onzas":
            return valor / 28.3495
    elif categoria == "Volumen":
        if conversion == "Galones a litros":
            return valor * 3.78541
        elif conversion == "Litros a galones":
            return valor / 3.78541
        elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
            return valor * 16.387
        elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
            return valor / 16.387
    elif categoria == "Tiempo":
        if conversion == "Horas a minutos":
            return valor * 60
        elif conversion == "Minutos a segundos":
            return valor * 60
        elif conversion == "Días a horas":
            return valor * 24
        elif conversion == "Semanas a días":
            return valor * 7
    elif categoria == "Velocidad":
        if conversion == "Millas por hora a kilómetros por hora":
            return valor * 1.60934
        elif conversion == "Kilómetros por hora a metros por segundo":
            return valor / 3.6
        elif conversion == "Nudos a millas por hora":
            return valor * 1.15078
        elif conversion == "Metros por segundo a pies por segundo":
            return valor * 3.28084
    elif categoria == "Área":
        if conversion == "Metros cuadrados a pies cuadrados":
            return valor * 10.7639
        elif conversion == "Pies cuadrados a metros cuadrados":
            return valor / 10.7639
        elif conversion == "Kilómetros cuadrados a millas cuadradas":
            return valor / 2.58999
        elif conversion == "Millas cuadradas a kilómetros cuadrados":
            return valor * 2.58999
    elif categoria == "Energía":
        if conversion == "Julios a calorías":
            return valor * 0.239006
        elif conversion == "Calorías a kilojulios":
            return valor / 239.006
        elif conversion == "Kilovatios-hora a megajulios":
            return valor * 3.6
        elif conversion == "Megajulios a kilovatios-hora":
            return valor / 3.6
    elif categoria == "Presión":
        if conversion == "Pascales a atmósferas":
            return valor / 101325
        elif conversion == "Atmósferas a pascales":
            return valor * 101325
        elif conversion == "Barras a libras por pulgada cuadrada":
            return valor * 14.5038
        elif conversion == "Libras por pulgada cuadrada a bares":
            return valor / 14.5038
    elif categoria == "Tamaño de datos":
        if conversion == "Megabytes a gigabytes":
            return valor / 1024
        elif conversion == "Gigabytes a Terabytes":
            return valor / 1024
        elif conversion == "Kilobytes a megabytes":
            return valor / 1024
        elif conversion == "Terabytes a petabytes":
            return valor / 1024

# Título de la app
st.title('Conversor de Unidades, por Andrés Arbeláez Morales')

# Descripción de la app
st.write('Selecciona una categoría y luego elige el tipo de conversión que deseas realizar.')

# Selección de categoría
categorias = [
    "Temperatura", "Longitud", "Peso/Masa", "Volumen", 
    "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos"
]
categoria = st.selectbox('Selecciona la categoría:', categorias)

# Dependiendo de la categoría, mostramos las opciones de conversión
if categoria == "Temperatura":
    conversiones = [
        "Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"
    ]
elif categoria == "Longitud":
    conversiones = [
        "Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"
    ]
elif categoria == "Peso/Masa":
    conversiones = [
        "Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"
    ]
elif categoria == "Volumen":
    conversiones = [
        "Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"
    ]
elif categoria == "Tiempo":
    conversiones = [
        "Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"
    ]
elif categoria == "Velocidad":
    conversiones = [
        "Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", 
        "Nudos a millas por hora", "Metros por segundo a pies por segundo"
    ]
elif categoria == "Área":
    conversiones = [
        "Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", 
        "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"
    ]
elif categoria == "Energía":
    conversiones = [
        "Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"
    ]
elif categoria == "Presión":
    conversiones = [
        "Pascales a atmósferas", "Atmósferas a pascales", 
        "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"
    ]
elif categoria == "Tamaño de datos":
    conversiones = [
        "Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"
    ]

# Selección del tipo de conversión
conversion = st.selectbox('Selecciona la conversión:', conversiones)

# Ingreso del valor a convertir
valor = st.number_input('Ingresa el valor a convertir:', min_value=0.0)

# Realizar la conversión y mostrar el resultado
if valor:
    resultado = convertir(valor, categoria, conversion)
    st.write(f'El resultado de la conversión es: {resultado}')
