from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    nome: Mapped[str] = mapped_column(String(10), nullable=False)