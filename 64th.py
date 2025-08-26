# Request API data
import requests
base_url = "https://pokeapi.co/api/v2/"
name = "mewtwo"
url = f"{base_url}/pokemon/{name}"
response = requests.get(url)
if response.status_code == 200:
            data = response.json()
            pokemon_name = "Mewtwo"
            pokemon_info = (data)
            img_url = data['sprites']['front_default']
            print(f"Name: {pokemon_info['name'].capitalize()}")
            print(f"ID: {pokemon_info['id']}")
            print("Image URL:",img_url)
            print(f"Height: {pokemon_info['height']}")
            print(f"Weight: {pokemon_info['weight']}")
        
else:
        print(f"Error: {response.status_code} - {response.reason}")   
