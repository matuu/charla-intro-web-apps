from pydantic import BaseModel


class Tarea(BaseModel):
    titulo: str
    descripcion: str
    terminada: bool = False
    id: int = 0