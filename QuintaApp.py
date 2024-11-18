import streamlit as st

# Título de la página
st.title("Refugio de Gatitos 🐱")

# Descripción
st.write("""
¡Bienvenidos al Refugio de Gatitos! 🏠🐾
Aquí encontrarás a los gatitos más adorables que están buscando un hogar lleno de amor.
¡Adóptalos y cambia su vida!

### ¿Quiénes somos?
Somos un refugio dedicado a la protección y bienestar de los gatos. Nuestro objetivo es rescatar, cuidar y encontrar hogares responsables para nuestros pequeños amigos.

### Nuestros Gatitos:
""")

# Lista de gatitos disponibles para adopción
if "gatitos" not in st.session_state:
    st.session_state.gatitos = [
        {"nombre": "Miau", "edad": "2 meses", "descripcion": "Un gatito juguetón y cariñoso."},
        {"nombre": "Luna", "edad": "1 año", "descripcion": "Le encanta acurrucarse y recibir mimos."},
        {"nombre": "Pelusa", "edad": "3 meses", "descripcion": "Muy activa y curiosa."},
        {"nombre": "Gato", "edad": "4 años", "descripcion": "Amante de la tranquilidad y las siestas."},
    ]

# Mostrar gatitos disponibles
for gatito in st.session_state.gatitos:
    st.write(f"**Nombre**: {gatito['nombre']}")
    st.write(f"**Edad**: {gatito['edad']}")
    st.write(f"**Descripción**: {gatito['descripcion']}")
    st.write("---")

# Formulario para registrar nuevos gatitos
st.header("Registrar Nuevo Gatito 📝")
nombre = st.text_input("Nombre del gatito")
edad = st.text_input("Edad del gatito")
descripcion = st.text_area("Descripción del gatito")

# Botón para agregar el gatito a la lista
if st.button("Registrar Gatito"):
    if nombre and edad and descripcion:
        nuevo_gatito = {"nombre": nombre, "edad": edad, "descripcion": descripcion}
        st.session_state.gatitos.append(nuevo_gatito)
        st.success(f"¡Gatito {nombre} registrado exitosamente!")
    else:
        st.warning("Por favor completa todos los campos.")

