import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
import database_connection


st.set_page_config(page_title="Bild-Upload-App", page_icon=":camera:", layout="wide")
st.title('Techlabs Document Scanner')

# Eingabemaske zur Auswahl des Bildes
file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "jpeg", "png"])

if file:
    image = file.getvalue()
    response = requests.post("http://localhost:5000/predict", data=image)
    st.write("Das hochgeladene Bild:", response.content)


def upload_image():
    uploaded_file = st.file_uploader("Wählen Sie ein Bild aus", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image_bytes = io.BytesIO(uploaded_file.read())
        database_connection.save_image(image_bytes)
        st.success("Bild erfolgreich hochgeladen!")

def delete_image():
    image_id = st.text_input("Geben Sie die ID des zu löschenden Bildes ein")
    if image_id:
        deleted = database_connection.delete_image(image_id)
        if deleted:
            st.success("Bild erfolgreich gelöscht")
        else:
            st.error("Fehler beim Löschen des Bildes")

def main():
    st.set_page_config(page_title="Bild-Uploader", page_icon=":camera:", layout="wide")
    st.title("Bild-Uploader")

    st.write("Laden Sie ein Bild hoch oder löschen Sie ein vorhandenes")
    upload_image_button = st.button("Bild hochladen")
    if upload_image_button:
        upload_image()

    delete_image_button = st.button("Bild löschen")
    if delete_image_button:
        delete_image()

if __name__ == '__main__':
    main()