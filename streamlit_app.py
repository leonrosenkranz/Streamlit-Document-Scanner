import streamlit as st
import pandas as pd
import numpy as np
import requests
import io
from PIL import Image
import tensorflow as tf
import keras
import sklearn
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import joblib

# Input interface for selection of the image

st.set_page_config(page_title="© 2023 mathSCAN", page_icon=":camera:", layout="wide")
st.title('TechLabs Document Scanner')

st.markdown("<br><hr style='border-top: 10px solid green'><br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Select an image of your mathematical expression", type=["jpg", "jpeg", "png"])
image = tf.io.read_file("C:/Users/Ayman/Documents/mathformula.png")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

st.markdown("<br><hr style='border-top: 10px solid green'><br>", unsafe_allow_html=True)

#Converts preprocessed Latex Formula back to String
def decodePreprocessedLatex(y_pred, label_encoder):
  filtered_token = list(filter(lambda x: x != 530, y_pred))
  y_decoded = label_encoder.inverse_transform(filtered_token)
  return ' '.join(y_decoded)


# Preprocessing

img_height = 825
img_width = 825

def encode_single_sample(img):
    #chane img_path correctly
    #img_path = pathOfDirectory + img_path
    # 1. Read image
    #img = tf.io.read_file(img_path)
    #2. Decode and convert to grayscale
    img = tf.io.decode_png(img, channels=1)
    # 3. Convert to float32 in [0, 1] range
    img = tf.image.convert_image_dtype(img, tf.float32)
    # 4. Resize to the desired size
    img = tf.image.resize_with_pad(img, img_height, img_width)
    # 5. Transpose the image because we want the time
    # dimension to correspond to the width of the image.
    img = tf.transpose(img, perm=[1, 0, 2])
    # 4. Map the characters in label to numbers
    img = tf.expand_dims(img,axis=0)
    # 5. Return a dict as our model is expecting two inputs
    #return {"image": img, "label": label}
    return img

#Label Encoder
encoder = joblib.load('label_encoder.joblib')
maximum_length = 206


# A utility function to decode the output of the network
def decode_batch_predictions(pred):
    input_len = np.ones(pred.shape[0]) * pred.shape[1]
    # Use greedy search. For complex tasks, you can use beam search
    results = keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][
        :, :maximum_length
    ]
    # Iterate over the results and get back the text
    output_text = []
    for res in results:
        res = tf.strings.reduce_join(decodePreprocessedLatex(res,encoder)).numpy().decode("utf-8")
        print(res)
        output_text.append(res)
    return output_text

model = keras.models.load_model("C:/Users/Ayman/Desktop/streamlit/Streamlit-Document-Scanner/Model/trainedModel")


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

batch_size = 1

img = encode_single_sample(image)
pred = model.predict(img,batch_size=1)
pred_decoded = decode_batch_predictions(pred)
print(pred_decoded)