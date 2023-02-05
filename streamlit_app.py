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


def upload_image():
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        return image
    return None

def remove_image():
    st.warning("Image has been removed.")

def main():
    st.set_page_config(page_title="Image Uploader", page_icon=":camera:", layout="wide")
    uploaded_image = upload_image()

    if uploaded_image is not None:
        st.sidebar.title("Actions")
        if st.sidebar.button("Remove Image"):
            remove_image()

if __name__ == "__main__":
    main()
