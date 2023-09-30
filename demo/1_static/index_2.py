from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <head>
            <title>Hola Mundo</title>
        </head>
        <body>
            <h1>Soy todo un hacker!</h1>
            <form method="post" action="/saluda">
                <input type="text" name="nombre" placeholder="Escriba su nombre" />
                <input type="submit" value="Saludar" />
            </form>
        </body>
    </html>
    """


@app.post("/saluda", response_class=HTMLResponse)
async def saluda(nombre: str = Form()):
    return f"""
    <html>
        <head>
            <title>Hola Mundo</title>
        </head>
        <body>
            <h1>Soy todo un hacker!</h1>
            <h2>Hola {nombre}! </h2>
        </body>
    </html>
    """
