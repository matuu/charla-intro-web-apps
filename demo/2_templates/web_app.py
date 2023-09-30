from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/saluda", response_class=HTMLResponse)
async def saluda(request: Request, nombre: str = Form()):
    return templates.TemplateResponse(
        "saluda.html",
        {"request": request, "nombre": nombre}
    )


@app.get("/about", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})