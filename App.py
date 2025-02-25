import streamlit as st
import time
import numpy as np
import pandas as pd

# --- CSS personnalisé ---
st.markdown("""
    <style>
        body {
            background-color : #f4f4f4;
        }

        .button {
            text-align: center;
            font-size: 40px;
            color: #3498db;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Titre ---
st.markdown("<h1 class='title'>Bienvenue sur mon premier site developpé en Python !</h1>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("Navbar")
page = st.sidebar.radio("Aller à :", ["Accueil", "Données", "Graphiques"])

# --- Sélection du thème ---
theme = st.sidebar.selectbox("Choisir un thème :", ["Bleu", "Vert", "Rouge"])

theme_colors = {
    "Bleu": "#3498db",
    "Vert": "#2ecc71",
    "Rouge": "#e74c3c"
}
color = theme_colors[theme]

st.markdown(f"<style> .title {{ color: {color}; }} </style>", unsafe_allow_html=True)

# --- Contenu de la page ---
if page == "Accueil":
    st.subheader("Accueil")
    st.write("Bienvenue sur cette application Streamlit avec du style !")

    # Bouton interractif
    if st.button("Clique moi !"):
        with st.spinner("Chargement..."):
            time.sleep(2)
        st.success("Bravo, tu as cliqué sur le bouton !")

    # Ajout d'une image
    st.image("https://source.unsplash.com/600x300/?nature,technology", caption="Une belle image dynamique")

elif page == "Données":
    st.subheader("Données aléatoires")
    df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])
    st.write(df)

elif page == "Graphiques":
    st.subheader("Graphique dynamique")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["X", "Y", "Z"])
    st.line_chart(chart_data)

# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>&copy; 2025 - Créé avec ❤ par Guillaume DUPUIS</p>
""", unsafe_allow_html=True)