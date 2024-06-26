from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .routers import todos, users

app = FastAPI()

# Postavljanje direktorija za HTML predloske
templates = Jinja2Templates(directory="app/templates")

# Uključivanje routera za zadatke i korisnike
app.include_router(todos.router)
app.include_router(users.router)

# Korijenska ruta koja prikazuje početnu stranicu
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
