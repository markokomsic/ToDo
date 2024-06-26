import bcrypt
from sqlalchemy.orm import Session
from . import models, schemas

# Funkcija za hashiranje lozinke
def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Funkcija za verifikaciju lozinke
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Dohvati korisnika po ID-u
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Dohvati korisnika po korisnickom imenu
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Kreiraj novog korisnika
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Dohvati sve zadatke za datog korisnika
def get_todos(db: Session, user_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.owner_id == user_id).all()

# Kreiraj novi zadatak
def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.TodoItem(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Azuriraj status zadatka
def update_todo_status(db: Session, todo_id: int, is_done: bool):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo:
        db_todo.is_done = is_done
        db.commit()
        db.refresh(db_todo)
    return db_todo

# Obrisi zadatak
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
