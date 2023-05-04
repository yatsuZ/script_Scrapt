# Pour afficher les graphique avec Streamlit j'ai du le faire en python
# Vous devez faire la commande : streamlit run statistic.py
import os
import importlib

if importlib.util.find_spec('streamlit') is None:
    print("Streamlit n'est pas installé. Il est en train de sinstaller !!\n\n")
    os.system("pip install streamlit")
else:
    print("Streamlit est déjà installé.")
import importlib

if importlib.util.find_spec('matplotlib') is None:
    print("Matplotlib n'est pas installé.  Il est en train de sinstaller !!\n\n")
    os.system("pip install matplotlib")
else:
    print("Matplotlib est déjà installé.")
    

import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Connexion à la base de données
conn = sqlite3.connect('Meteo_France_Mensuelle.db')

# Requête SQL pour extraire les données 
query = "SELECT region, annee, mois, temperature_moyenne, vitesse_vent, precipitations_moyennes, duree_jour  FROM Meteo_France_Mensuelle"

# Utilisation de pandas pour exécuter la requête et stocker les résultats dans un DataFrame
df = pd.read_sql_query(query, conn)

# Création d'une colonne de date au format AAAA-MM
df["date"] = df.apply(lambda row: str(row["annee"]) + "-" + str(row["mois"]), axis=1)

st.write("Il y a d'autres données dans la base de données")

# Affichage du DataFrame
st.write(df[["region", "date", "temperature_moyenne", "vitesse_vent", "precipitations_moyennes", "duree_jour"]])

#####

# Création d'une nouvelle colonne pour stocker la durée du jour en format numérique
df["duree_jour_numeric"] = 0.0

# Parcours de chaque ligne du DataFrame
for index, row in df.iterrows():
    # Récupération de la valeur de la colonne "duree_jour"
    duree_jour = row["duree_jour"]
    
    # Conversion de la chaîne de caractères en un nombre flottant représentant le nombre total d'heures de la journée
    heures, minutes, secondes = map(float, duree_jour.split(":"))
    duree_jour_numeric = heures + minutes / 60 + secondes / 3600
    
    # Stockage de la durée du jour en format numérique dans la nouvelle colonne
    df.at[index, "duree_jour_numeric"] = duree_jour_numeric

# Groupement des données par région
df_grouped = df.groupby("region")

# Parcours de chaque groupe et tracé des graphiques correspondants
for name, group in df_grouped:
    fig, ax = plt.subplots()
    ax.bar(group["date"], group["duree_jour"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Durée du jour (en heures)")
    ax.set_title(f"Durée du jour par région - {name}")
    st.pyplot(fig)

##

# Groupement des données par région
df_grouped = df.groupby("region")

# Configuration du graphique
fig, ax = plt.subplots(figsize=(24, 8))  # taille de 12x8 pouces

# Parcours de chaque groupe et tracé des graphiques correspondants
for name, group in df_grouped:
    color = plt.cm.tab20(df_grouped.groups[name].size / len(df))
    ax.plot(group["date"], group["temperature_moyenne"], label=name, color=color)

# Configuration de l'axe des x
ax.set_xticklabels(df["date"].unique(), rotation=45)

# Configuration du graphique
ax.set_xlabel("Période (année-mois)")
ax.set_ylabel("Température moyenne (en degrés Celsius)")
ax.legend()

# Configuration de la taille de la figure
fig.set_size_inches(24, 8)

# Affichage du graphique
st.pyplot(fig)



