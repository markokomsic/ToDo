from pydantic import BaseModel
from typing import Optional

# Model za JWT token
class Token(BaseModel):
    access_token: str
    token_type: str

# Model za podatke iz JWT tokena
class TokenData(BaseModel):
    username: Optional[str] = None

# Osnovni model za korisnika
class UserBase(BaseModel):
    username: str

# Model za kreiranje novog korisnika
class UserCreate(UserBase):
    password: str

# Model za prikaz korisnika
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

# Osnovni model za zadatak
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

# Model za kreiranje novog zadatka
class TodoCreate(TodoBase):
    pass

# Model za ažuriranje zadatka
class TodoUpdate(TodoBase):
    is_done: Optional[bool] = False

# Model za prikaz zadatka
class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
