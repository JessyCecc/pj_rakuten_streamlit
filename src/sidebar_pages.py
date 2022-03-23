import streamlit as st
import awesome_streamlit as awst
import src.sections.page_context as p_context
import src.sections.page_dataviz as p_dataviz
import src.sections.page_classification_textes as p_class_txts
import src.sections.page_classification_images as p_class_imgs
import src.sections.page_conclusion as p_conclusion


# ----- ----- ----- ----- -----


def get_pages():
    pages = {
        "Projet et contexte": p_context,
        "Audit des données - DataViz": p_dataviz,
        "Classification - Textes": p_class_txts,
        "Classification - Images": p_class_imgs,
        "Projet conclusion": p_conclusion,
    }
    return pages


def render():
    # create a sidebar and set the title
    st.sidebar.title("Projet Rakuten")

    # select page from dictionary
    pages_dic = get_pages()

    # initialize sidebar with page dictionary
    select_page = st.sidebar.radio("", list(pages_dic.keys()))

    # selected page by user or first from dictionary by default
    page_current = pages_dic[select_page]

    with st.spinner(f"Chargement  de la page {select_page} ..."):
        awst.shared.components.write_page(page_current)

    st.sidebar.text(" ")
    st.sidebar.info(
        "Réalisation : Jean-Christophe CECCALDI\n"
        "Mentor : Gaspard GRIMM\n"
        "Promotion : Formation continue Juin 2021"
    )
