from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    nome: str
    tipo: str