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
    st.image("https://s1.qwant.com/thumbr/474x471/2/b/d1c948303c6fd54ca3c1d7e59a6f2902ddc3df1e628453d8c42eaec4f7b65d/th.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%3Fid%3DOIP.PGo9E8zB952jEpBStbVAcwHaHX%26pid%3DApi&q=0&b=1&p=0&a=0", caption="Une belle image dynamique")

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
