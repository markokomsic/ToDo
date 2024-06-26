# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Inicijalizacija baze podataka
def init_db():
    import app.models  # Uvezi modele
    Base.metadata.create_all(bind=engine)

# Kreiranje baze podataka
if __name__ == "__main__":
    init_db()
