import streamlit as st
import pandas as pd

CT_URL_X_TRAIN = 'https://drive.google.com/file/d/1l3E32b-7V_ADAnTrXcaTiBFDWLZh3mxz/view?usp=sharing'


@st.cache
def load_dataframe(url, rows_max=100000):
    df = pd.read_csv(url, nrows=rows_max, index_col=0)
    return df


def get_dataframe():
    path_x_train = CT_URL_X_TRAIN
    path_x_train = 'data/X_train_update.csv'
    df_x_train = load_dataframe(path_x_train)
    # st.subheader('DataFrame')
    # st.write(df_x_train)
    return df_x_train