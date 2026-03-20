import requests

def buscar_pokemon(nome: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Pokémon não encontrado")

    data = response.json()

    species_url = data["species"]["url"]
    species_response = requests.get(species_url)
    species_data = species_response.json()

    descricao = None
    for entry in species_data["flavor_text_entries"]:
        if entry["language"]["name"] == "en":
            descricao = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
            break

    return {
        "id": data["id"],
        "nome": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "habilidades": [h["ability"]["name"] for h in data["abilities"]],
        "stats": {
            stat["stat"]["name"]: stat["base_stat"]
            for stat in data["stats"]
        },
        "sprite": data["sprites"]["front_default"],
        "descricao": descricao
    }