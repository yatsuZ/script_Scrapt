<h1 style="display:flex; align-items:center">
        script_Scrapt <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Left.png" alt="Magnifying Glass Tilted Left" width="25" height="25" style="margin-left:10px;">
</h1>

<h2 style="display:flex; align-items:center"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Chequered%20Flag.png" alt="Chequered Flag" width="60" />  Somaire</h2>

- [Introduction](./README.md#Introduction)
- [1ier Script](./README.md#Scrapper_des_données)

---

## Introduction

Il sagit d'un repo pedagogique sur le scraping. Voila ce que je dois faire :

```
Le projet consiste à créer 3 scripts 

- Un scrapper générant des données sous forme de tableaux

- Un script capable d’ingérer les données dans la bdd

- Affichage des donnes sur streamlit(tableau, 2 -3 graphiques qui représente vos donnes)
```

C'est un travil de groupe je le fais avec mon ami Abdel (faire un lien vers le github d'Abdel).

## Scrapper des données

Alors qu'es que scrapper ?

> Le scrapping ou le scraping (en français : extraction de données) consiste à récupérer automatiquement des informations ou des données à partir d'un site web ou d'une autre source en ligne en utilisant des programmes informatiques appelés "scraper" ou "web scraper". Ces données peuvent être collectées pour des raisons d'analyse, de recherche ou pour alimenter une base de données.

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Warning.png" alt="Warning" width="25" height="25" /> Mais attention !!
cela peut etre illégalle de scrapper des données il faut faire attention et verifier les politique de chaque site web.

<h3>Quoi Scrapper</h3>

Sincerement c'est la partie qui demande le plus le temp de reflexion haha 😅.
Nous allons scrapper ce site web: https://www.historique-meteo.net/france/ .
Il s'agit un site web archivant les meteos de continent pays etc.
Voila un exemple de ce que nous esseyrons de reucpérer :

| ID | Région | Année | Mois | Température moyenne | Température maximale | Température minimale | Température maximale maximum | Température minimale maximum | Température minimale minimum | Vitesse du vent | Température du vent | Précipitations moyennes par jour | Record de précipitations sur une journée | Humidité | Visibilité | Couverture nuageuse | Heure du lever du soleil | Heure du coucher du soleil | Durée du jour |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0 | les Alpes | 2023 | JANVIER | -3 | 1 | -7 | 16 | 9 | -26 | 10km/h | -11 | 1mm | 11mm | 90% | 9km | 50% | 08:18:00 | 17:45:00 | 9:27:0 |

La technologie utilise sere la librairie panda et beautiful soup. Avec Python Bien sure
