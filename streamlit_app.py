import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
from PIL import Image




# Eingabemaske zur Auswahl des Bildes

st.set_page_config(page_title="Bild-Upload-App", page_icon=":camera:", layout="wide")
st.title('TechLabs Document Scanner')

st.markdown("<br><hr style='border-top: 10px solid green'><br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Wählen Sie ein Bild aus", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Credits

st.markdown("<br><hr style='border-top: 10px solid green'><br>", unsafe_allow_html=True)
st.markdown("An AI solution by TechLabs X <span style='color: green'>math</span>SCAN®", unsafe_allow_html=True)
st.image("C:\Users\leon.rosenkranz\Documents\Studium\Techlabs\Git repository\Streamlit-Document-Scanner\Icons\TechLabs.png")


