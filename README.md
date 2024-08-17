# ue19_labo09-10
# Application de Blagues avec Python

## Description
Ce projet interroge une API publique pour récupérer une blague et l'afficher dans la console.

## Prérequis
- Python 3
- Docker (si vous souhaitez utiliser Docker)

## Installation
1. Clonez ce repository :
   git clone https://github.com/Q220080/ue19_labo09-10.git
   cd ue19_labo09-10

  
2. Installez les dépendances Python :
   pip install -r requirements.txt


## Utilisation
Lancez le script Python :
   python app.py

## Utilisation avec Docker
1. Construisez l'image Docker :
   docker build -t blague-app .
2. Exécutez le conteneur :
   docker run --rm blague-app

## API utilisée
Nous utilisons l'API [JokeAPI](https://v2.jokeapi.dev/) pour récupérer une blague au hasard.


   
