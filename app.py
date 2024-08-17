import requests

def get_pun():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"  # URL d'une API publique de blagues
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get("joke", "Aucune blague trouvée!")
    else:
        return "Impossible d'obtenir une blague."

if __name__ == "__main__":
    print("Voici une blague :")
    print(get_pun())
