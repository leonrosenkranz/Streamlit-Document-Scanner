import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
from PIL import Image


st.set_page_config(page_title="Bild-Upload-App", page_icon=":camera:", layout="wide")
st.title('Techlabs Document Scanner')

# Eingabemaske zur Auswahl des Bildes
file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "jpeg", "png"])

if file:
    image = file.getvalue()
    response = requests.post("http://localhost:5000/predict", data=image)
    st.write("Das hochgeladene Bild:", response.content)


uploaded_file = st.file_uploader("Wählen Sie ein Bild aus", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

