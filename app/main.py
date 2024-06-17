from fastapi import FastAPI
from app.routers import todos
from app.database import init_db

init_db()

app = FastAPI()

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ToDo API"}
