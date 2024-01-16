import streamlit as st 
paragraph="Le cerveau est l'une, sinon la partie la plus importante de notre corps. Toute maladie impliquant le cerveau est très grave. Il est très important de détecter une tumeur de manière précise et aussi tôt que possible. Notre tâche consistera à prendre des images par résonance magnétique (IRM) et à prédire avec précision si l'image du cerveau contient une tumeur."
pa="Une tumeur cérébrale est une masse ou une croissance de cellules anormales dans votre cerveau."
pk="Il existe de nombreux types différents de tumeurs cérébrales. Certaines tumeurs cérébrales sont non cancéreuses (bénignes), tandis que d'autres sont cancéreuses (malignes). Les tumeurs cérébrales peuvent commencer dans votre cerveau (tumeurs cérébrales primaires), ou le cancer peut commencer dans d'autres parties de votre corps et se propager à votre cerveau sous forme de tumeurs cérébrales secondaires (métastatiques)."
aa="Les options de traitement des tumeurs cérébrales dépendent du type de tumeur cérébrale que vous avez, ainsi que de sa taille et de son emplacement."
ze="Le but de ce projet sera de créer un modele CNN capable de classifier une IRM du cerveau en quatre  catégories . Nous commencerons par un modèle de base. Ensuite, nous appliquerons transfert learning pour améliorer la précision. L'idée est que la précision s'améliorera à chaque étape"
def main():
    # st.title("streamlit hello ")
    st.text("Encadré par : Hajar Moussnif")
    # import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #EEE3CB;
        color: white;
    }
    .stApp {
        background-color: #EEE3CB;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Décoration pour attirer l'attention
st.markdown(
    """
    <style>
    .highlight-section {
        padding: 10px;
        background-color: #9BABB8;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 20px;
    }

    .highlight-section h1 {
        color: black;
    }

    .highlight-text {
        padding: 10px;
        background-color: #9BABB8;
        border-radius: 5px;
        margin-bottom: 20px;
    }

    .highlight-text p {
        color: black;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Section de la page avec décoration pour attirer l'attention
st.markdown('<div class="highlight-section"><h1>Cancer classification from MRI images</h1></div>', unsafe_allow_html=True)

# Le reste de votre code Streamlit
# ...

# Chemins d'accès des images fictives
image1_path = "ss.png"
image2_path = "gfg.png"
image3_path = "kj.png"

# Affichage des images côte à côte dans la même ligne
col1, col2 = st.columns(2)
with col1:
    st.image(image1_path, use_column_width=True)
with col2:
    st.image(image2_path, use_column_width=True)

# Zone de texte
st.markdown("---")
st.markdown('<div class="highlight-text"><p> Introduction </p></div>', unsafe_allow_html=True)
st.write(paragraph)
st.write(pa)
st.write(pk)
# st.write(pr)
st.write(aa)
# Affichage du texte saisi au milieu de la page avec une écriture en gras et une couleur blanche
st.markdown("---")
st.markdown('<div class="highlight-text"><p style="text-align: center; font-weight: bold;">Objectif du projet </p></div>', unsafe_allow_html=True)
st.write(ze)

# Partie de la page avec titre, description et bouton décorés
st.markdown('<div class="highlight-text"><p>Les quatres catégories </p></div>', unsafe_allow_html=True)
st.image(image3_path, use_column_width=True)
# if st.button("Cliquez ici pour être redirigé"):
#     # URL de redirection
#     url = "https://www.kaggle.com/code/ruslankl/brain-tumor-detection-v1-0-cnn-vgg-16"
#     # Redirection vers l'URL
#     st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)
# st.markdown('<div class="highlight-text"><p> Models used </p></div>', unsafe_allow_html=True)
# texte = st.text("voici les informations concernant notre projet hhhhhhzjhx iudhnzdx okqhdj")
# ###################################################################################""

if __name__ == '__main__' :
    main()
    ##########################################################""
    # import streamlit as st

# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #F5EFE7;
#         color: white;
#     }
#     .stApp {
#         background-color: #F5EFE7;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Décoration pour attirer l'attention
# st.markdown(
#     """
#     <style>
#     .highlight-section {
#         padding: 10px;
#         background-color: #4F709C;
#         border-radius: 5px;
#         text-align: center;
#         margin-bottom: 20px;
#     }

#     .highlight-section h1 {
#         color: black;
#     }

#     .highlight-text {
#         padding: 10px;
#         background-color: #D8C4B6;
#         border-radius: 5px;
#         margin-bottom: 20px;
#     }

#     .highlight-text p {
#         color: black;
#         text-align: center;
#         font-weight: bold;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Section de la page avec décoration pour attirer l'attention
# st.markdown('<div class="highlight-section"><h1>Cancer classification from MRI images</h1></div>', unsafe_allow_html=True)

# # Le reste de votre code Streamlit
# # ...

# # Chemins d'accès des images fictives
# image1_path = "ss.png"
# image2_path = "gfg.png"

# # Affichage des images côte à côte dans la même ligne
# col1, col2 = st.columns(2)
# with col1:
#     st.image(image1_path, use_column_width=True)
# with col2:
#     st.image(image2_path, use_column_width=True)

# # Zone de texte
# st.markdown("---")
# st.markdown('<div class="highlight-text"><p>introduction :</p></div>', unsafe_allow_html=True)
# texte = st.text("voici les informations concernant notre projet hhhhhhzjhx iudhnzdx okqhdj")

# # Affichage du texte saisi au milieu de la page avec une écriture en gras et une couleur blanche
# st.markdown("---")
# st.markdown('<div class="highlight-text"><p style="text-align: center; font-weight: bold;">Datasets introduction :</p></div>', unsafe_allow_html=True)
# texte1 = st.text("voici les informations concernant notre projet hhhhhhzjhx iudhnzdx okqhdj")

# # Partie de la page avec titre, description et bouton décorés
# st.markdown('<div class="highlight-text"><p> where did we find the data ?</p></div>', unsafe_allow_html=True)
# texte = st.text("voici les informations concernant notre projet hhhhhhzjhx iudhnzdx okqhdj")
# if st.button("Cliquez ici pour être redirigé"):
#     # URL de redirection
#     url = "https://www.kaggle.com/code/ruslankl/brain-tumor-detection-v1-0-cnn-vgg-16"
#     # Redirection vers l'URL
#     st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)
# st.markdown('<div class="highlight-text"><p> Models used </p></div>', unsafe_allow_html=True)
# texte = st.text("voici les informations concernant notre projet hhhhhhzjhx iudhnzdx okqhdj")
# ###################################################################################""