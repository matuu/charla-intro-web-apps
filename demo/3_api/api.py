from fastapi import FastAPI

from db import DB
from models import Tarea

todo_db = DB()
todo_db.insert(
    Tarea(titulo="Tarea 1", descripcion="Hacer andar FastAPI"))
todo_db.insert(
    Tarea(titulo="Tarea 2", descripcion="Entender como funciona pydantic")
)

app = FastAPI()


@app.get("/", response_model=list[Tarea])
async def tarea_listar():
    return todo_db.get_all()


@app.post("/", response_model=Tarea)
async def tarea_crear(tarea: Tarea):
    return todo_db.insert(tarea)


@app.get("/{id}", response_model=Tarea)
async def tarea_detalles(id: int):
    try:
        return todo_db.get(id)
    except KeyError:
        return {}


@app.put("/{id}", response_model=Tarea)
async def tarea_actualizar(id: int, tarea: Tarea):
    return todo_db.update(id, tarea)


@app.delete("/{id}")
async def tarea_eliminar(id: int):
    return todo_db.delete(id)
