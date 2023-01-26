import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('penyakit_obesitas.sav','rb'))

# judul web
st.title('Prediksi Penyakit Obesitas')