import streamlit as st

st.title("Bienvenue sur le site web de Samira")
ville_choisie = st.selectbox(
    "Indiquez votre arrondissement de récupération",
    options=["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"],
)
villes = {
    "Manhattan": "images/Manhattan.jpg",
    "Brooklyn": "images/Brooklyn.jpg",
    "Queens": "images/Queens.jpg",
    "Bronx": "images/Bronx.jpg",
    "Staten Island": "images/staten-island.webp",
}
st.write(f"Tu as choisi : **{ville_choisie}**")

st.image(villes[ville_choisie], caption=ville_choisie, use_container_width=True)
