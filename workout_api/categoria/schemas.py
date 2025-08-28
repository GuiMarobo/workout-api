from typing import Annotated
from pydantic import BaseModel, Field

class Categoria(BaseModel):
    nome : Annotated[str, Field(description='Nome da Categoria', examples='Boxe', max_length=10)]