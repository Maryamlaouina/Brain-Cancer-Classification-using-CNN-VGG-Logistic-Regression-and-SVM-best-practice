import streamlit as st 
paragraphh="En parallèle, nous avons également utilisé des approches sans apprentissage profond, telles que la régression logistique et le SVM, pour la classification du cancer à partir d'images IRM. Pour ces approches, nous avons extrait des caractéristiques à partir des images en utilisant des descripteurs tels que les histogrammes de gradients orientés (HOG) et les caractéristiques de texture basées sur la transformée de Fourier."
parag="Nous avons utilisé la régression logistique avec une régularisation L2 et un paramètre de pénalité C égal à 1, ainsi que le SVM avec un noyau linéaire et un paramètre de régularisation C égal à 1. Nous avons entraîné ces modèles sur les caractéristiques extraites à partir des images d'entraînement et avons ajusté les hyperparamètres à l'aide de la validation croisée pour améliorer leurs performances."
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
# st.markdown('<div class="highlight-section"><h1>Cancer classification from MRI images</h1></div>', unsafe_allow_html=True)

# Le reste de votre code Streamlit
# ...

# Chemins d'accès des images fictives
# image1_path = "ss.png"
image2_path = "trf.png"
# image3_path = "gfg.png"

# Affichage des images côte à côte dans la même ligne
# col1, col2 = st.columns(2)
# with col1:
#     st.image(image1_path, use_column_width=True)
# with col2:
#     st.image(image2_path, use_column_width=True)

# Zone de texte
# st.markdown("---")
# st.markdown('<div class="highlight-text"><p> Aperçu de la tâche </p></div>', unsafe_allow_html=True)
# st.write(paragraph)
# st.write(para)
# st.write(pa)
# st.write(pk)
# st.write(pr)
# st.write(aa)
# Affichage du texte saisi au milieu de la page avec une écriture en gras et une couleur blanche
st.markdown("---")
st.markdown('<div class="highlight-text"><p style="text-align: center; font-weight: bold;"> Apprentissage profondeur (CNN et VGG16) </p></div>', unsafe_allow_html=True)
st.image(image2_path, use_column_width=True)
# st.write(paragraphh)

# Partie de la page avec titre, description et bouton décorés
st.markdown('<div class="highlight-text"><p> Svm et Logistic regression  </p></div>', unsafe_allow_html=True)
# st.image(image3_path, use_column_width=True)
# st.text("vous pouvez télécharger datasets à partir de link suivant")
st.write(paragraphh)
st.write(parag)

# if st.button("lien de téléchargement"):
#     # URL de redirection
#     url = "https://www.kaggle.com/code/ruslankl/brain-tumor-detection-v1-0-cnn-vgg-16"
#     # Redirection vers l'URL
#     st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)

# ###################################################################################""

# if __name__ == '__main__' :
#     main()
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