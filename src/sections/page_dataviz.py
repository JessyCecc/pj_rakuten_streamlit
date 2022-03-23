import pandas as pd
import streamlit as st

import src.tools.dataframe as t_data
import src.tools.statistics as stats
import src.tools.html as html

# ----- ----- ----- ----- -----


def write():
    st.title("DataViz - Data Visualization")
    st.text(
        "Les données proposées dans le cadre du projet restent la propriété exclusive\n"
        "de Rakuten Institute of Technology.\n"
        "Elles sont constituées d’approximativement 99k produits de différentes catégories."
    )
    st.text(
        "Les données d’entrainement comportent 84916 articles et de test 13812 articles."
    )

    # --- TRAIN - Dataset ---
    df_X_train = t_data.get_X_train()
    df_Y_train = t_data.get_Y_train()

    st.subheader("Jeu de données d'entrainement")

    t_data.render(df_X_train, title="Features - variables d'entrée")
    st.text(
        'Nous constatons que les "Features" variables d''entrée sont de 2 types :\n'
        '-  des variables textuelles, colonnes "designation" et "description."\n'
        '-  des données de type image donc le nom du fichier dépend des colonnes "productid" et "imageid".'
    )
    st.text(
        'Des données sont manquantes pour la variable description.'
    )
    t_data.render_info(df_X_train)

    t_data.render(df_Y_train, title="Target - variable cible")
    st.text(
        'Nous constatons que les "Targets" sont les identifiants des catégories de classe d''article.'
    )
    st.text(
        'Aucune donnée n''est manquante.'
    )
    t_data.render_info(df_Y_train)

    # ----- ----- ----- ----- -----
    # --- TEST - Dataset ---
    df_X_test = t_data.get_X_test()

    st.subheader("Jeu de données de test")

    t_data.render(df_X_test, title="Features - variables d'entrée")
    st.text(
        'Comme pour les données d''entrainement, des descriptions sont manquantes.'
    )
    t_data.render_info(df_X_test)

    # ----- ----- ----- ----- -----
    # --- Statistics - Missing Description ---
    percent_X_train_missing = stats.dataframe_percent_of_missing(df_X_train, "description")[0]
    percent_X_test_missing = stats.dataframe_percent_of_missing(df_X_test, "description")[0]

    st.subheader("Pourcentage des descriptions manquantes.")
    st.text(
        f"Entrainement : {percent_X_train_missing} %\n"
        f"Test : {percent_X_test_missing} %"
    )

    # ----- ----- ----- ----- -----
    # --- Les classes de catégories ---
    st.subheader("Filtrage des classes de catégories à partir de la variable cible.")
    code_list = list(df_Y_train.prdtypecode.unique())
    st.text(
        f"Liste des {len(code_list)} identifiant de catégorie : \n"
        f"{code_list}"
    )

    # ----- ----- ----- ----- -----
    # --- Generate an index by category class ---
    # target_labels_list = [n for n in range(len(code_list))]
    # df_prdtypecode_target = pd.DataFrame({'prdtypecode': code_list, 'target': target_labels_list})
    # t_data.render(df_prdtypecode_target, title="Création d'une table de correspondance avec les targets.")
    df_Y_train_target = t_data.get_Y_train_target()
    t_data.render(
        df_Y_train_target,
        title="Affection d'un index unique par classe de catégorie.",
        text="Creation d'une table de correspondance identifiant / index et ajout d'une colonne target au dataset de test."
    )

    # ----- ----- ----- ----- -----
    # --- Graphique de répartion du nombre d'article par classe ---
    st.subheader("Répartition des articles par classe de catégories")
    st.image('images/10_countplot_products_by_target.jpg')

    st.image("images/repartition_products_categories.png")
    st.image("images/repartition_percent_products_categories.png")

    html.text("Nous pouvons constater que les catégories les moins représentées ont pour la plupart un bon pourcentage de description renseignée. Il sera donc important de garder la colonne description.")
    html.text("Il est donc nécessaire de garder la colonne description. Nous prenons la décision de concaténer les 2 colonnes dans un nouvelle colonne « texts ».")

    st.text("Nous pourrons appliquer différents filtres comme :")
    st.text("•  la conversion en minuscule.")
    st.text("•  la conversion des caractères accentués ou spéciaux.")
    st.text("•  les tags du language HTML  (plus spécifiquement la description).")
    st.text("•  application d'une tokenization et suppression des stopwords.")

    st.subheader("Nombre de mots par texte après filtrage")
    st.image("images/repartition_textes_filtered.png")
    st.image("images/repartition_textes_filtered_100.png")

    st.subheader("Axe d'amélioration possible")

    html.text("• &nbsp; Dans le but de réduire le nombre de mot par texte nous pouvons également ne prendre en compte que la colonne « designation ». Car les données sont plus propres et mots obtenus après traitement sont plus pertinent.")
    html.text("• &nbsp; Nous pouvons mettre en place une traduction de tous mots en anglais avant d’utiliser la fonctionnalité de « stopwords ». En utilisant une librairie tel que « google_trans_new ».")
    html.text("• &nbsp; Essayer de réduire le nombre de mots pris en compte en ajoutant des mots au dictionnaire « stopwords », comme « aa » qui a été rencontré (probablement suite au traitement).")
    html.text("• &nbsp; Nous pourrions effectuer des obtimisations telle que « Lemmatization » / « Stemming », que nous n’avons pas pu mettre en place faute de temps.")

    # ----- ----- ----- ----- -----
    # --- Les classes de catégories ---
    st.subheader("Les features de type image.")

    html.text("Un aperçu de 5 images d'articles pour chaques catégories")

    for i in range(27):
        st.image(f"images/img_cat_{i}.png")


    html.text(
        "Dans une première observation, on constate que les objets sont très diversifiés pour une même catégorie d’article.")
    html.text("Des objets apparaissent détourés sur fond blanc et d’autres sont sur un fond d’ambiance ou de paysage.")
    html.text("Certaines images apparaissent comme des miniatures avec une bordure blanche très épaisse.")
    html.text("Les catégories peuvent contenir des objets assez similaires comme :", margin_bottom=False)
    html.text(
        "- &nbsp; 'livres_adulte' (10),  'magazines' (2280), 'livres_et_illustres' (2705) et 'livres_jeunesse' (2403)",
        margin_bottom=False)
    html.text("- &nbsp; 'goodies_geek'  (1140)  et 'figurines_wargames' (1180)", margin_bottom=False)
    html.text("- &nbsp; 'jeux_videos_dematerialises' (2905) et 'jeux_videos_import' (40)")
    html.text(
        "Il y a donc une très forte disparité des images dans toutes les catégories ce qui rendra le traitement et la classification plus compliqué.")



