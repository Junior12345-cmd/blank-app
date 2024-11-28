import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("🎈 Analyse des données Iris")


# En-tête de l'application (rendu avec Markdown)
'''
# :earth_americas: TP Streamlit Dashboards réalisé par Junior SANNI(Master IFRI 2024-2025)
'''

# Ajout d'un espace vide pour une mise en page plus aérée
''
''

# Composant Streamlit pour uploader un fichier CSV
file = st.file_uploader("Importer vos données ici", type=["csv"])

# Vérification si un fichier a été téléchargé
if file is not None:
    # Lecture du fichier CSV dans un DataFrame Pandas
    df = pd.read_csv(file)
    
    # Affichage des premières lignes du DataFrame
    st.dataframe(df.head())
    
    # Résumé statistique des données
    st.subheader("Résumé statistique")
    st.write(df.describe())

    # Informations sur le DataFrame
    st.subheader("Structure des données")
    buffer = f"Nombre de lignes : {df.shape[0]}\nNombre de colonnes : {df.shape[1]}"
    st.text(buffer)    

    # Sélection des colonnes numériques
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_columns:
        st.subheader("Distribution des colonnes numériques")
        for col in numeric_columns:
            fig, ax = plt.subplots()
            df[col].plot(kind='hist', bins=20, title=f"Distribution de {col}", ax=ax)
            st.pyplot(fig)

    # Affichage des valeurs manquantes
    st.subheader("Valeurs manquantes")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])
