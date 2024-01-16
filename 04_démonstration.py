import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
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
st.markdown('<div class="highlight-section"><h1>Démonstration </h1></div>', unsafe_allow_html=True)
#######################################################################################""

import streamlit as st
import tensorflow as tf
from PIL import Image
# import cv2
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('cnn_model.h5')

# Define the classes
classes = ['glioma_tumor','meningioma_tumor','no_tumor','pituitary_tumor']

# Create the web application
st.title("Brain Cancer Classification")
# st.write("Upload an MRI image for classification")

# Function to preprocess the image
def preprocess_image(image):
    img = image.resize((150, 150))
    img = np.array(img)
    # img = np.expand_dims(img, axis=0)
    img = img.reshape(1,150,150,3)
    return img

# User input - file upload
uploaded_file = st.file_uploader("Charger l'image MRI pour La classification", type=["jpg", "jpeg", "png"])

# Perform classification on uploaded image
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI', use_column_width=True)

    # Preprocess the image
    preprocessed_img = preprocess_image(image)

    # Make predictions
    prediction = model.predict(preprocessed_img)
    predicted_class = classes[prediction.argmax()]

    # a=model.predict(img_array)
    # indices = a.argmax()
    # indices

    # Display the prediction
    st.write('Prediction:')
    st.write(f'Class: {predicted_class}')
    st.write(f'Confidence: {prediction[0][np.argmax(prediction)]}')
