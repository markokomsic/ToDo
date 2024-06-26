from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

# Tajni ključ za potpisivanje JWT-a
SECRET_KEY = "fsre"
# Algoritam koji se koristi za potpisivanje JWT-a
ALGORITHM = "HS256"
# Vrijeme trajanja pristupnog tokena (u minutama)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Funkcija za kreiranje pristupnog tokena
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    # Ako je specificirano trajanje tokena, koristi ga
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    # U suprotnom, koristi zadano trajanje
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    # Kreiranje i enkodiranje JWT-a
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Funkcija za verifikaciju tokena
def verify_token(token: str, credentials_exception):
    try:
        # Dekodiranje JWT-a
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Dohvaćanje korisničkog imena iz payload-a
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
