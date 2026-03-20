from fastapi import FastAPI
from app.api import pokemon

app = FastAPI()

app.include_router(pokemon.router)