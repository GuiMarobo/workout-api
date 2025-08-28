from typing import Annotated
from pydantic import BaseModel, Field

class CentroTreinamento(BaseModel):
    nome : Annotated[str, Field(description='Nome do Centro de Treinamento', examples='Marega Fight Club', max_length=20)]
    endereco : Annotated[str, Field(description='Endereço do Centro de Treinamento', examples='R. José Angelo, 59 - Aurora', max_length=60)]
    proprietario : Annotated[str, Field(description='Proprietário do Centro de Treinamento', examples='Marcinho', max_length=30)]