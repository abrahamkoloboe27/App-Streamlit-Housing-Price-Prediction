import streamlit as st
import requests

# Configurer la page
st.set_page_config(
    page_title="Prédiction du Prix des Maisons",
    page_icon=":house_with_garden:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Ajouter du CSS personnalisé
st.markdown("""
    <style>
    /* Style pour le fond de la page */
    .main {
        background-color: #f5f5f5;
    }
    /* Style pour la barre latérale */
    .sidebar .sidebar-content {
        background-color: #e6e6e6;
    }
    /* Style pour le bouton de soumission */
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        padding: 0.5em 1em;
        border-radius: 5px;
    }
    /* Style pour les en-têtes */
    h1, h2, h3 {
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Ajouter un titre avec un emoji
st.title(":house_with_garden: **Prédiction du Prix des Maisons**")

# Section de l'auteur dans la barre latérale
if st.sidebar.checkbox("À propos de l'auteur"):
    with st.expander("Auteur", True):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image("img/About the author.png", width=150)
        with c2:
            st.header("**S. Abraham Z. KOLOBOE**")
            st.markdown("""
                *<span style='color:blue'>Data Scientist | Ingénieur en Mathématiques et Modélisation</span>*

                Bonjour,

                Je suis Abraham KOLOBOE, un Data Scientist et Ingénieur en Mathématiques et Modélisation. 
                Mon expertise se situe dans les domaines des sciences de données et de l'intelligence artificielle. 
                Avec une approche technique et concise, je m'engage à fournir des solutions efficaces et précises dans mes projets.
                        
                * **Email** : [abklb27@gmail.com](mailto:abklb27@gmail.com)
                * **WhatsApp** : +229 91 83 84 21
                * **LinkedIn** : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)
            """, unsafe_allow_html=True)

# Définir le point de terminaison de l'API
API_ENDPOINT = st.sidebar.text_input("Point de terminaison de l'API", value="https://abrahamklb-housing-api.hf.space/predict")

# Définir l'application Streamlit
def main():
    # Ajouter des descriptions dans la barre latérale
    with st.sidebar:
        if st.checkbox("Afficher la description du projet", value=True):
            st.markdown("""
                ### Description du Projet
                Ce projet est une application de prédiction des prix des maisons qui utilise un modèle d'apprentissage automatique pour prédire le prix d'une maison en fonction de diverses caractéristiques telles que la superficie, le nombre de chambres, de salles de bains, etc.
            """)

        if st.checkbox("Afficher la description de l'application", value=True):
            st.markdown("""
                ### Description de l'Application
                Cette application permet aux utilisateurs de saisir les détails d'une maison et d'obtenir un prix prédit basé sur le modèle d'apprentissage automatique. Les utilisateurs peuvent également modifier le point de terminaison de l'API pour utiliser un modèle différent si désiré.
            """)

    # Créer un formulaire
    st.header("Entrez les détails de la maison")
    with st.form(key="house_form"):
        # Créer deux colonnes
        col1, col2 = st.columns(2)

        # Champs de saisie dans la première colonne
        with col1:
            area = st.number_input("Superficie (en pieds carrés)", value=2640, min_value=0)
            bedrooms = st.number_input("Chambres", value=2, min_value=0, step=1)
            bathrooms = st.number_input("Salles de bains", value=1, min_value=0, step=1)
            stories = st.number_input("Étages", value=1, min_value=0, step=1)
            mainroad = st.selectbox("Route Principale", ["yes", "no"])
            guestroom = st.selectbox("Chambre d'Amis", ["yes", "no"])
            basement = st.selectbox("Sous-sol", ["yes", "no"])

        # Champs de saisie dans la deuxième colonne
        with col2:
            hotwaterheating = st.selectbox("Chauffage à Eau Chaude", ["yes", "no"])
            airconditioning = st.selectbox("Climatisation", ["yes", "no"])
            parking = st.number_input("Parking", value=1, min_value=0, step=1)
            prefarea = st.selectbox("Zone Préférée", ["yes", "no"])
            furnishingstatus = st.selectbox("État d'Ameublement", ["furnished", "unfurnished", "semi-furnished"])

        # Créer un dictionnaire avec les données saisies
        data = {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": mainroad,
            "guestroom": guestroom,
            "basement": basement,
            "hotwaterheating": hotwaterheating,
            "airconditioning": airconditioning,
            "parking": parking,
            "prefarea": prefarea,
            "furnishingstatus": furnishingstatus,
        }

        # Bouton de soumission
        submit_button = st.form_submit_button(label="Prédire")

    # Envoyer une requête POST à l'API et afficher le prix prédit
    if submit_button:
        with st.spinner('Prédiction en cours...'):
            try:
                response = requests.post(API_ENDPOINT, json=data)
                response.raise_for_status()
                prediction = response.json()["prediction"]
                # Afficher le prix prédit avec le symbole de l'euro
                st.success(f"Le prix prédit est : **{prediction:,.2f} €**")
            except requests.exceptions.RequestException as e:
                st.error(f"Erreur lors de l'appel à l'API : {e}")

if __name__ == "__main__":
    main()
