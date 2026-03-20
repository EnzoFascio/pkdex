pokemons_db = [
    {"id": 1, "nome": "Pikachu", "tipo": "Elétrico"},
    {"id": 2, "nome": "Charmander", "tipo": "Fogo"},
]

def listar_pokemons():
    return pokemons_db

def buscar_por_id(pokemon_id: int):
    for p in pokemons_db:
        if p["id"] == pokemon_id:
            return p
    return None

def criar_pokemon(pokemon):
    pokemons_db.append(pokemon)
    return pokemon