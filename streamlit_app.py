import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
from PIL import Image




# Eingabemaske zur Auswahl des Bildes

st.set_page_config(page_title="Bild-Upload-App", page_icon=":camera:", layout="wide")
st.title('Techlabs Document Scanner')
st.markdown("TechLabs X <span style='color: green'>math</span>SCAN®", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Wählen Sie ein Bild aus", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)



