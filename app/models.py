from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Model za korisnika
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Povezivanje sa zadacima
    todos = relationship("TodoItem", back_populates="owner")

# Model za zadatak
class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    is_done = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Povezivanje sa korisnikom
    owner = relationship("User", back_populates="todos")
