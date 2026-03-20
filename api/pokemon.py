from fastapi import APIRouter
from app.service import pokemon_service
from app.schemas.pokemon_schema import Pokemon
from fastapi import FastAPI
from app.api import pokemon

app = FastAPI()
router = APIRouter()

app.include_router(pokemon.router)

@app.get("/")
def root():
    return {"mensagem": "Pokedex API rodando"}


@router.get("/pokemon/{nome}")
def buscar(nome: str):
    return pokemon_service.buscar_pokemon(nome)

@router.get("/pokemon")
def listar():
    return pokemon_service.listar()

@router.get("/pokemon/{pokemon_id}")
def buscar(pokemon_id: int):
    return pokemon_service.buscar(pokemon_id)

@router.post("/pokemon")
def criar(pokemon: Pokemon):
    return pokemon_service.criar(pokemon.dict())

@router.get("/pokemon/search")
def search(nome: str):
    return pokemon_service.buscar_por_nome(nome)