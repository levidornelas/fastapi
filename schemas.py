from datetime import date
from pydantic import BaseModel
from enum import Enum

#Os Schemas serão os models criados usando Pydantic que servirão para a validação dos dados que serão inseridos no 'banco de dados.'

class Authors(Enum):
  KMF = 'kmf'
  JUBILEU = 'jubileu'
  JAMAICA = 'jamaica'

class SpinOffs(BaseModel):
  nome: str
  release: date

class FilmBase(BaseModel):
  id: int
  nome: str
  autor: str
  spinoffs: list[SpinOffs] = []

class FilmCreate(FilmBase):
  pass

class FilmWithID(FilmBase):
  id: int