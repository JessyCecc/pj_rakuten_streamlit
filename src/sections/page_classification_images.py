import streamlit as st
import src.tools.html as html

# ----- ----- -----


def write():
    st.title("Classification des images")

    html.text(
        "Il est un fait que les images sont complexes et très diversifiées, ainsi il devient obligatoire d’utiliser un modèle basé sur l’apprentissage profond ou « Deep Learning ». Les derniers travaux ont prouvé que les modèles basés sur les réseaux de neurones convolutifs ont donnés les meilleurs résultats.")


    st.subheader("Apprentissage par transfert")
    st.image("images/modeles_chart_diff.png")
    html.text(
        "L’entraînement d’un modèle de réseaux de neurones convolutifs (CNN) prendrait beaucoup de temps avant d’avoir un résultat satisfaisant, nous pouvons nous tourner vers l’apprentissage par transfert.")
    html.text(
        "Le principe de la méthode et d’utilisé les couches convolutives du modèle pré-entraîné en gelant « freeze » les poids associés aux couches convolutives. Celles-ci étant déjà entraînés à la reconnaissance des caractéristiques « feature extraction ».")
    html.text(
        "Le choix du modèle est une étape importante en effet de nombreux modèles CNN sont disponibles, il n’est pas facile de choisir. En essayant de s’appuyer cet <a href='https://theaisummer.com/cnn-architectures/'>Article</a>.")
    html.text(
        "Nous pouvons à partir de ce graphique avoir aperçu du nombre d’opération par époque (Operations [G-FLOPs] et le nombre de paramètres (entre 1M et 150M) en fonction de la performance (Top-1 accuracy).")
    html.text("Nous portons notre choix sur le modèle déjà pré-entraîné ImageNet.")

    st.subheader("Les hyperparamètres")
    html.text("Le choix des hyperparamètres :")
    html.text(
        "•	Chargement des couches et poids du modèle vgg16, dont les couches seront gelées. Nous utiliserons par la suite les modèles Xception et Resnet")
    html.text(
        "•	La configuration des couches de dropout est configurée à 20%, il pourrait être intéressant de les faire varier car elles exercent une forte régularisation et limite le sur-apprentissage.")
    html.text("•	Pour l’optimiseur nous avons choisi « Nadam » avec un learning_rate de 0.01")
    html.text(
        "•	Learning rate, nous le configurons à 0.01, ce réglage détermine la taille du pas à chaque itération, l’augmenter réduit le temps de calcul mais nous perdons en optimisation.")
    html.text(
        "•	Batch size et epochs, c’est 2 paramètres dépendent énormément des données en entrée, en fonction de leurs configurations, (article), nous choisissons 32.")


    st.subheader("Architecture et entraînement")

    html.text(
        "Utilisation de l’augmentation des données sur les images en utilisant la librairie de Tensorflow.Keras – ImageDataGenerator.")
    html.text("Doc : Tensorflow Keras ImageDataGenerator")
    html.text(
        "Le principe est d’augmenter le nombre d’image en entrée en appliquant des filtres tel que les déformations horizontales, verticales ou par cisaillement, zoom, rotation, ou recadrage. ")
    html.text("Toutes les couches du modèle pré-entraîner seront gelés.")

    html.text(
        "Architecture avec le modèle pré-entrainer VGG16",
        justify=False, style="font-size:20px;font-weight:bold;"
    )
    st.image("images/archi_model_vgg16.png")

    html.text(
        "Architecture avec le modèle pré-entrainer Xception",
        justify=False, style="font-size:20px;font-weight:bold;"
    )
    st.image("images/archi_model_xception.png")

    html.text(
        "Architecture avec le modèle pré-entrainer Resenet50",
        justify=False, style="font-size:20px;font-weight:bold;"
    )
    st.image("images/archi_model_resnet50.png")


    st.subheader("Tableau des résultats obtenus des modèles")
    html.text(
        "Le tableau ci-dessous permettra de retracer les performances des différents modèles que nous entraînerons.")
    html.text(
        "Nous avons manqué de temps pour entrainer les modèles sur Colab. Sur nos machines cela faisait tomber le kernel. Les hyperparamètres ou la configuration de l’architecture du modèle était probablement trop imposante pour nos machines.")
    html.text("Test de performance avec un jeu de données de 8000 images max :")
    html.text("- &nbsp; Learning rage : 0.01")
    html.text("- &nbsp; Batch size : 32")
    html.text("- &nbsp; Optimizer : Nadam")
    html.text("- &nbsp; Jeux de données")
    st.image("images/classification_images_cross_modele_reports.jpg")


    st.subheader("Performance avec les callbacks")
    html.text(
        "Afin de mieux maîtriser l’entraînement des modèles, il faudrait ajouter les callbacks, dans le but de suivre plus finement l’apprentissage. Les callbacks les plus utilisés :")
    html.text(
        "• &nbsp; EarlyStopping : souvent utilisé et qui permet de surveiller les metrics et d’arrêter l’entraînement si celle-ci cessent de s’améliorer.")
    html.text(
        "• &nbsp; ModelCheckpoint : il nous permet de sauvegarder le modèle régulièrement pendant l’entraînement. Il surveille et enregistre des points de contrôle à intervalles réguliers en fonction des mesures configurées.")
    html.text(
        "• &nbsp; TensorBoard : permet de visualiser le résumé de l’entraînement et de générer des logs. Ces derniers pourront par la suite être visualiser dans TensorBoard pour visualiser la progression de l’entraînement.")
    html.text(
        "• &nbsp; LearningRateScheduler : permet de mettre à jour le « learning rate » au fur et à mesure que l’entraînement progresse. Cela permet de l’adapter au bout d’un certain nombre d’époque par exemple. ")
    html.text(
        "• &nbsp; CSVLogger : il enregistre les détails de l’entraînement dans un fichier CSV. Les paramètres enregistrés sont « epoch, accurancy, loss, val_accurancy, val_loss ». La précision doit être passée comme une métrique lors de la compilation du modèle pour être prise en compte, dans le cas contraire une erreur d’exécution peut sur-venir.")
    html.text("• &nbsp; LambdaCallback : il permet d’appeler une fonction personnalisée sur l’en des évènements.")
    html.text(
        "• &nbsp; ReduceLROnPlateau : utilisé pour modifier le « learning rate » lorsque les métriques ont cessé de s’améliorer. Contrairement à LearningRateScheduler il réduira l’apprentissage basé sur la métrique et non sur l’Epoch.")
    html.text("• &nbsp; RemoteMonitor : utile lorsque l’on souhaite envoyer des logs dans une API.")


    st.subheader("Conclusion")
    html.text("Il existe de nombreux axes d’amélioration et d’optimisation :")
    html.text("• &nbsp; Ajuster les paramètres d’augmentation des données, afin d’avoir un plus grand jeu de données.")
    html.text("• &nbsp; Amélioration et rééquilibrage du jeu de données d’entraînement.")
    html.text("• &nbsp; Ajouter des callback afin de mieux monitorer l’entraînement de nos modèles.")
    html.text("• &nbsp; Ajuster les couches convolutives non gelées.")
    html.text("• &nbsp; Augmenter la taille et le nombre de couches denses cachées.")
    html.text("• &nbsp; Modifier dans les couches denses le taux des couches Dropout.")
    html.text("• &nbsp; Ajuster / modifier les fonctions de perte.")
    html.text("• &nbsp; Ajuster la taille du batch et le nombre d’epoch.")
    html.text("• &nbsp; Essayer différent optimiseur, bien que Adam semble être un choix pertinent.")




