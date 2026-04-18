from typing import List, Optional
from .schemas import LibroCreate, LibroUpdate, LibroRead

db_libros: List[LibroRead] = []
id_counter = 1

def crear_libro(data: LibroCreate) -> LibroRead:
    global id_counter
    nuevo_libro = LibroRead(id=id_counter, **data.model_dump())
    db_libros.append(nuevo_libro)
    id_counter += 1
    return nuevo_libro

def obtener_todos() -> List[LibroRead]:
    return db_libros

def eliminar_libro(id: int) -> bool:
    global db_libros
    for index, libro in enumerate(db_libros):
        if libro.id == id:
            db_libros.pop(index) # Elimina el libro de la lista
            return True
    return False