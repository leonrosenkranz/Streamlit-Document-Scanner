import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
from PIL import Image


def first_page():
    st.write("Willkommen auf der ersten Seite")
    if st.button("Zur zweiten Seite wechseln"):
        second_page()

    st.set_page_config(page_title="Bild-Upload-App", page_icon=":camera:", layout="wide")
    st.title('Techlabs Document Scanner')

    # Eingabemaske zur Auswahl des Bildes
    file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "jpeg", "png"])

    if file:
        image = file.getvalue()
        response = requests.post("http://localhost:5000/predict", data=image)
        st.write("Das hochgeladene Bild:", response.content)

def second_page():
    st.write("Willkommen auf der zweiten Seite")
    if st.button("Zurück zur ersten Seite"):
        first_page()

first_page()




