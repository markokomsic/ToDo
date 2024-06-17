from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

def get_todos(db: Session = SessionLocal()):
    return db.query(models.TodoItem).all()

def create_todo(todo: schemas.TodoCreate, db: Session = SessionLocal()):
    db_todo = models.TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
