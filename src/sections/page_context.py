import streamlit as st

import src.tools.html as html

# ----- ----- -----


def write():
    st.title("Contexte du projet")

    st.subheader("Actualité")
    html.text("C’est un projet réalisé dans le cadre du challenge Rakuten France Multimodal Product Data Classification, organisé par Rakuten Institute of Thechnology Paris, et mis en ligne sur le site ChallengeData.")
    html.text("Projet très ambitieux faisant appel aux différentes technologies du Deep Learning. Telles que le NLP (Natural Language Processing), la vision par ordinateur – CV (Computer Vision), les réseaux de neurones récurrents,  NNR (Recurrent Neural Network) ou les réseaux convolutifs, CNN (Convolutif Neural Network).")
    html.text("Le sujet est d’actualité, d’autant plus que le marché de la vente en ligne est en forte croissance. Les boutiques ont de plus en plus besoin d’automatisé les informations des articles qu’elles mettent en vente. La crise du COVID n’a fait que renforcer cet état de fait.")
    html.text("Au niveau technique, ce projet s’intègre parfaitement parmi les recherches actuelles des grandes plateformes mutualisés d’e-commerçants. Les problématiques de classification ou de labélisation à grande échelle d’article en sont une parfaite représentation.")

    st.subheader("Cadre de la formation")
    html.text("Au niveau apprentissage, ce projet s’intègre parfaitement à l’apprentissage du langage Python et des nombreuses librairies comme Tensorflow / Keras et Natural Langage Tookit illustrant les différents cours dispensés chez DataScientest.com.")
    html.text("C’est une excellente prise en main et mise en pratique des cours, même si personnellement le temps m’a vraiment manqué pour approfondir le sujet et obtenir de bien meilleures performances avec les modèles.")

    st.title("Objectif")
    html.text("L’objectif et la classification d’article d’un catalogue, a partie de données textuelles et d’images. Chaque produit doit être associé à une catégorie issue du catalogue Rakuten, en réduisant le plus possible les erreurs.")


