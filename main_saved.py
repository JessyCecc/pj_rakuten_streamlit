import streamlit as st
import pandas as pd

import src.use_dataframe_train

header = st.container()
contexte = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title('Projet Rakuten\nMultimodal Data Classification')
    st.text('')


with contexte:
    st.header('Contexte du projet')
    st.text('C’est un projet réalisé dans le cadre du challenge Rakuten France Multimodal Product Data Classification, organisé par Rakuten Institute of Thechnology Paris, et mis en ligne sur le site ChallengeData.')


with dataset:
    st.header('sub title Dataset')
    with st.echo():
        x = 17  # this
        y = 13
        z = (x + y) / 2
    st.write("z: ", z)
    st.write(f"Result for z: {z}")


with features:
    st.header('sub title Features')



with modelTraining:
    st.header('sub title Model Training')


