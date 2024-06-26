from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .routers import todos, users

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.include_router(todos.router)
app.include_router(users.router)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
