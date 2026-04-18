from fastapi import FastAPI
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.biblioteca.router import routers as biblioteca_router

from fastapi import FastAPI
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
# 1. Agregamos el import (fijate que tu archivo se llama router.py y la variable routers)
from app.modules.biblioteca.router import routers as biblioteca_router 

def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 1",
        version="1.0.0"
    )
    
    app.include_router(producto_router)
    app.include_router(categoria_router)

    # 2. Pasamos la variable biblioteca_router aquí:
    app.include_router(biblioteca_router)
    
    return app

app = create_app()