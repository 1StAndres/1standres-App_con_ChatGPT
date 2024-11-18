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

# Imágenes de gatitos
st.image("https://www.petfinder.com/wp-content/uploads/2019/10/Kittens-Are-the-Purest-Form-of-Happiness-1-750x500.jpg", caption="Gatitos buscando un hogar", use_column_width=True)

# Lista de gatitos disponibles para adopción
gatitos = [
    {"nombre": "Miau", "edad": "2 meses", "descripcion": "Un gatito juguetón y cariñoso."},
    {"nombre": "Luna", "edad": "1 año", "descripcion": "Le encanta acurrucarse y recibir mimos."},
    {"nombre": "Pelusa", "edad": "3 meses", "descripcion": "Muy activa y curiosa."},
    {"nombre": "Gato", "edad": "4 años", "descripcion": "Amante de la tranquilidad y las siestas."},
]

for gatito in gatitos:
    st.write(f"**Nombre**: {gatito['nombre']}")
    st.write(f"**Edad**: {gatito['edad']}")
    st.write(f"**Descripción**: {gatito['descripcion']}")
    st.write("---")

# Información de contacto
st.write("""
### ¡Contáctanos!
Si te gustaría adoptar o saber más, puedes contactarnos en:
- **Email**: refugio.gatitos@ejemplo.com
- **Teléfono**: 123-456-7890
""")



