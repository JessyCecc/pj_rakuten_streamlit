import streamlit as st

import src.tools.html as html


# ----- ----- ----- ----- -----


def write():
    st.title("Classification des textes")




    st.subheader("Architecture des modèles")

    html.text("LSTM :  Long Short-Term Memory", margin_bottom=False, style="font-size:20px;font-weight:bold;")
    html.text(
        "Cette cellule se compose de 3 portes, ou zone de calculs qui régulent le flot d’informations (actions spécifiques) et un état en sortie.", margin_bottom=False)
    html.text("Forget gate (porte d’oubli)", margin_bottom=False)
    html.text("Input gate (porte d’entrée)", margin_bottom=False)
    html.text("Output gate (porte de sortie)", margin_bottom=False)
    html.text(
        "Ce réseau doit deviner ce qu’il doit retenir dans un vecteur à la volée, en stockant le fait qu’une information est importante ou non.")

    st.image("images/achi_model_lstm.png")

    html.text("GRU : Gate Recurrent Unit", margin_bottom=False, style="font-size:20px;font-weight:bold;")
    html.text("Cette cellule se compose de 2 portes et un état en sortie.", margin_bottom=False)
    html.text("Reset gate (porte de reset)", margin_bottom=False)
    html.text("Update gate (porte de mise à jour)", margin_bottom=False)
    html.text(
        "Les calculs effectués sont plus rapides et plus simples, ses résultats sont à comparés avec ceux de LSTM.")

    st.image("images/achi_model_gru.png")

    html.text("Bidirectional LSTM : ", margin_bottom=False, style="font-size:20px;font-weight:bold;")
    html.text(
        "Ce modèle recevra des observations sur le passé pour essayer d’améliorer les prédictions. Le modèle s’entraine à la fois sur une séquence et son inverse en entrée.")

    st.image("images/achi_model_bilstm.png")

    html.text("Conv 1D :", margin_bottom=False, style="font-size:20px;font-weight:bold;")
    html.text(
        "Etant donné le prétraitement effectué sur les mots, les phrases n’ont plus de sens réel, ainsi un modèle convolutif peut tout à fait être utilisé.", margin_bottom=False)
    html.text("Il est d’ailleurs plus rapide à entrainer que les modèles RNN.")

    st.image("images/achi_model_conv1d.png")


    st.subheader("Hyperparamètres")

    html.text("Ordre de grandeur des hyperparamètres testés :", margin_bottom=False)
    html.text("• &nbsp; Batch size : tests effectués sur 1000 et 200 pour Bi-LSTM", margin_bottom=False)
    html.text("• &nbsp; Epochs : entre 20 et 30", margin_bottom=False)
    html.text("• &nbsp; Optimizer : tests avec « adam » et « nadam »", margin_bottom=False)
    html.text("• &nbsp; Fonction de pertes et métriques : ", margin_bottom=False)
    html.text(" &nbsp; &nbsp; o &nbsp; Accuracy", margin_bottom=False)
    html.text(" &nbsp; &nbsp; o &nbsp; F1-score")


    st.subheader("Entraînement et évaluation")

    html.text("Modèle - LSTM", margin_bottom=False, style="font-size:20px;font-weight:bold;")

    # LSTM
    st.image("images/train_model_lstm.png")
    st.image("images/histo_model_lstm.png")
    st.image("images/cm_model_lstm.png")
    html.text("Etrangement nous avons obtenus d'assez mauvais résultats comparé aux autres modèles. Probablement un problème de paramétrage.")

    # GRU
    st.image("images/train_model_gru.png")
    st.image("images/histo_model_gru.png")
    st.image("images/cm_model_gru.png")
    html.text("Nous pouvons constater des confusions entre les classes « 4 et 0 », « 8 et 3 », « 14 et 8 », « 21 et 8 ». Dans l’ensemble les classes 0, 3 et 8 donnent le plus d’erreur de catégorisations.")

    # CONV1D
    st.image("images/train_model_conv1d.png")
    st.image("images/histo_model_conv1d.png")
    st.image("images/cm_model_conv1d.png")
    html.text("Nous pouvons constater des confusions entre les classes « 3 et 13 », « 4 et 0 », « 8 et 3 ». Ce modèle fait moins d’erreur de catégorisation que GRU sur les classes « 0, 3 et 8 »")

    # BILSTM
    st.image("images/train_model_bilstm.png")
    st.image("images/histo_model_bilstm.png")
    st.image("images/cm_model_bilstm.png")
    html.text("Nous pouvons constater des confusions entre les classes « 4 et 0 », « 10 et 0 », « 0 et 1 », « 8 et 3 », « 3 et 14 », « 17 et 7 » ainsi que « 16 et 17 ».")


    st.subheader("Performances et conclusion")

    html.text("Nos modèles semblent en général tomber rapidement en sur-apprentissage « overfitting ».")
    html.text(
        "Il faudrait revoir les hyperparamètres et les ajuster en conséquence mais également retravailler les données textuelles en entrée.")
    html.text("Nous obtenons des performances à peine satisfaisantes par report aux benchmark attendu du challenge.")
    html.text("Ci-dessous les performances de nos modèles sur le jeu de test.")

    st.image("images/classification_texts_cross_modele_reports.jpg")

    html.text("Le modèle Bi-LSTM aurait du nous donner un meilleur résultat, les hyperparamètres devront être ajusté.")
    html.text("Il existe de nombreux axes d’amélioration et d’optimisation :")
    html.text(
        "•	Réduire le nombre de mot pris en compte, en ne prenant pas en compte la description qui contient trop de mot parasite.")
    html.text(
        "•	Mettre en place une statistique des mots les plus souvent rencontrés par classe de catégorie et ajouter aux dictionnaires « stopwords » les mots les moins récurrents afin de ne garder que l’essentiel des mots pertinent d’une classe.")
    html.text("•	Utiliser d’autres optimizer différent de « Adam » et « Nadam »")

