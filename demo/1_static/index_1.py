from fastapi import FastAPI
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
        </body>
    </html>
    """
