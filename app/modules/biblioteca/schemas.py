from pydantic import BaseModel, Field
from typing import Optional

class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=100, example="La importancia de llamarse Ernesto")
    autor: str = Field(..., min_length=2, max_length=100, example="Oscar Wilde")
    anio_publicacion: int = Field(..., gt=1000, le=2026, example=1895)
    
class LibroCreate(LibroBase):
    pass

class LibroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=2, max_length=100, example="La importancia de llamarse Ernesto")
    autor: Optional[str] = Field(None, min_length=2, max_length=100, example="Oscar Wilde")
    anio_publicacion: Optional[int] = Field(None, gt=1000, le=2026, example=1895)

class LibroRead(LibroBase):
    id: int