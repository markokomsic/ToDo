from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from .. import schemas, crud, models
from ..database import SessionLocal, engine
from ..auth import verify_token

models.Base.metadata.create_all(bind=engine)

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Funkcija za dohvacanje sesije baze podataka
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Funkcija za dohvacanje trenutnog korisnika iz kolačića
def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Niste autenticirani",
            headers={"WWW-Authenticate": "Bearer"},
        )
    credentials_exception = HTTPException(
        status_code=401,
        detail="Nije moguće potvrditi vjerodajnice",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = verify_token(token.split(" ")[1], credentials_exception)
    user = crud.get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user

# Ruta za prikaz svih zadataka
@router.get("/todos", response_class=HTMLResponse)
def read_todos(request: Request, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    todos = crud.get_todos(db, user_id=current_user.id)
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})

# Ruta za kreiranje novog zadatka
@router.post("/todos", response_class=HTMLResponse)
def create_todo(request: Request, title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if not title or not description:
        raise HTTPException(status_code=400, detail="Naslov i opis ne mogu biti prazni.")
    crud.create_todo(db=db, todo=schemas.TodoCreate(title=title, description=description), user_id=current_user.id)
    return RedirectResponse(url="/todos", status_code=303)

# Ruta za ažuriranje statusa zadatka
@router.post("/todos/{todo_id}/update", response_class=HTMLResponse)
def update_todo(request: Request, todo_id: int, is_done: bool = Form(False), db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    crud.update_todo_status(db=db, todo_id=todo_id, is_done=is_done)
    return RedirectResponse(url="/todos", status_code=303)

# Ruta za brisanje zadatka
@router.post("/todos/{todo_id}/delete", response_class=HTMLResponse)
def delete_todo(request: Request, todo_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    crud.delete_todo(db=db, todo_id=todo_id)
    return RedirectResponse(url="/todos", status_code=303)
