# Request API data

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    requests.get(url)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.reason}")    

pokemon_name = "Mewtwo"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
