import streamlit as st
import pandas as pd
import numpy as np

# Seite 1
def page_1():
    st.write("Willkommen auf Seite 1")
    st.write("Klicken Sie auf den Button, um zu Seite 2 zu wechseln")
    if st.button("Zu Seite 2 wechseln"):
        page_2()

# Seite 2
def page_2():
    st.write("Willkommen auf Seite 2")
    st.write("Klicken Sie auf den Button, um zu Seite 1 zurückzukehren")
    if st.button("Zurück zu Seite 1"):
        page_1()

# Startseite
page_1()


st.title('Techlabs Document Scanner')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

