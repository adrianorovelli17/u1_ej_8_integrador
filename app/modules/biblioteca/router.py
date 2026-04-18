from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List, Optional
from . import schemas, services

routers = APIRouter(prefix='/libros', tags=['Biblioteca'])

# router.py
@routers.get("/", response_model=List[schemas.LibroRead])
def listar_libros():
    return services.obtener_todos()

@routers.post("/", response_model=schemas.LibroRead, status_code=status.HTTP_201_CREATED)
def crear_libro(libro: schemas.LibroCreate):
    return services.crear_libro(libro)

@routers.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_libro(id: int = Path(..., gt=0, title="ID del libro a eliminar")):
    fue_eliminado = services.eliminar_libro(id)
    
    if not fue_eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="El libro con ese ID no existe en la biblioteca"
        )
    
    return None



