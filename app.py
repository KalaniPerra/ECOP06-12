import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    'ECOP06',
    'https://unifei.edu.br/wp-content/uploads/2020/12/cropped-simbolo_VOLUME-1-32x32.png'
)

st.title('Página Demo ECOP06')

esportes = pd.read_csv('https://github.com/MainakRepositor/Datasets/raw/master/GeneralEsportData.csv', encoding='latin-1')

st.dataframe(esportes)

//