from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)