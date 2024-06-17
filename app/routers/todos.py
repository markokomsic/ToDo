from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Todo, TodoCreate
from app.crud import get_todos, create_todo

router = APIRouter()

@router.get("/todos", response_model=List[Todo])
def read_todos():
    return get_todos()

@router.post("/todos", response_model=Todo)
def add_todo(todo: TodoCreate):
    return create_todo(todo)
