import io

import streamlit as st
import pandas as pd

from src.config.files_dataset import Files_dataset

# ----- ----- ----- ----- -----

files_dataset = Files_dataset()


@st.cache
def load_dataframe(url, rows_max=100000):
    df = pd.read_csv(url, nrows=rows_max, index_col=0)
    return df


def get_dataframe(filename):
    path_x_train = f'data/{filename}'
    df_x_train = load_dataframe(path_x_train)
    return df_x_train


def get_X_train(): return get_dataframe(files_dataset.X_train)
def get_X_test(): return get_dataframe(files_dataset.X_test)
def get_Y_train(): return get_dataframe(files_dataset.Y_train)
def get_Y_train_target(): return get_dataframe(files_dataset.Y_train_target)


def render(df, title=None, text=None, head=5):
    shape = df.shape
    if head is not None:
        df = df.head(head)
    else:
        head = shape[0]
    if title is not None:
        st.subheader(title)
    if text is not None:
        st.text(text)
    else:
        st.text(f"Dimensions : ({shape[0]} x {shape[1]})"
                f" - extrait des {head} premieres lignes.")
    st.write(df)


def render_info(df, in_code=True):
    buffer = io.StringIO()
    df.info(buf=buffer)
    if in_code:
        st.code(buffer.getvalue())
    else:
        st.text(buffer.getvalue())
