import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
from PIL import Image


# Input interface for selection of the image

st.set_page_config(page_title="Bild-Upload-App", page_icon=":camera:", layout="wide")
st.title('TechLabs Document Scanner')

st.markdown("<br><hr style='border-top: 10px solid green'><br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Select an image of your mathematical expression", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

st.markdown("<br><hr style='border-top: 10px solid green'><br>", unsafe_allow_html=True)


# Credits

image_url = "https://techlabs.org/static/tl-logo-white-b4f7f9cac2eabf0e15d37fc9be3db918.png"
st.image(image_url, width=400)
st.markdown("© 2023 - TechLabs X <span style='color: green'>math</span>SCAN®", unsafe_allow_html=True)
st.markdown("<h2>Get in contact</h2><br>", unsafe_allow_html=True)

linkedin_url_ayman = "https://de.linkedin.com/in/ayman-soultana-3408a5192"
linkedin_url_joshua = "https://de.linkedin.com/in/josua-goecking"
linkedin_url_tobias = "https://de.linkedin.com/in/tobias-averbeck-771390157"
linkedin_url_leon = "https://www.linkedin.com/in/leon-rosenkranz-1b7997225/"

text = (
    f"<p style='color: white;'><a style='color: white;' href='{linkedin_url_ayman}'>Ayman Soultana</a></p>"
    f"<p style='color: white;'><a style='color: white;' href='{linkedin_url_joshua}'>Joshua Göcking</a></p>"
    f"<p style='color: white;'><a style='color: white;' href='{linkedin_url_tobias}'>Tobias Averbeck</a></p>"
    f"<p style='color: white;'><a style='color: white;' href='{linkedin_url_leon}'>Leon Rosenkranz</a></p>"
)

st.markdown(text, unsafe_allow_html=True)