# ToDo Web Aplikacija

Ovo je jednostavna ToDo web aplikacija izgrađena s FastAPI, SQLite i Jinja2 templatingom. Aplikacija podržava registraciju korisnika, prijavu te CRUD operacije za upravljanje zadacima.

## Značajke

- **Registracija i prijava korisnika**: Omogućava korisnicima kreiranje novog računa i prijavu postojećih korisnika.
- **Autentifikacija temeljem JWT-a**: Sigurno upravljanje korisničkim sesijama koristeći JSON Web Token (JWT).
- **Kreiranje, čitanje, ažuriranje i brisanje (CRUD) zadataka**: Korisnici mogu dodavati, pregledavati, ažurirati i brisati svoje zadatke.
- **Jinja2 templating za prikaz HTML stranica**: Koristi Jinja2 za dinamičko generiranje HTML stranica.

## Opis Fajlova

- `app/main.py`: Ulazna točka za FastAPI aplikaciju.
- `app/models.py`: Definicija SQLAlchemy modela za korisnike i zadatke.
- `app/schemas.py`: Pydantic modeli za validaciju podataka.
- `app/crud.py`: Funkcije za CRUD operacije nad bazom podataka.
- `app/database.py`: Konfiguracija za bazu podataka.
- `app/auth.py`: Funkcije za generiranje i provjeru JWT tokena.
- `app/routers/todos.py`: Rute za upravljanje zadacima.
- `app/routers/users.py`: Rute za registraciju i prijavu korisnika.
- `templates/`: Direktorij sa HTML šablonima.



## Korištenje
- **Registracija**
Posjetite /register rutu kako biste kreirali novi korisnički račun.

- **Prijava**
Posjetite /login rutu kako biste se prijavili sa svojim korisničkim imenom i lozinkom.

- **Upravljanje zadacima**
Nakon prijave, bit ćete preusmjereni na /todos rutu gdje možete kreirati, ažurirati i brisati svoje zadatke.

### Dokumentacija API-ja
FastAPI automatski generira dokumentaciju za sve API rute. Dokumentaciju možete pregledati i testirati API putem Swagger UI na `/docs`.



## Instalacija

### 1. Klonirajte repozitorij
Klonirajte repozitorij na svoje računalo koristeći git:
    
    
    git clone https://github.com/markokomsic/ToDo.git
    cd ToDo


### 2. Postavite virtualno okruženje
Kreirajte i aktivirajte virtualno okruženje:
    
    python -m venv .venv
    source .venv/bin/activate  # Na Windowsima koristite '.venv\Scripts\activate'


### 3. Instalirajte potrebne pakete
Instalirajte potrebne pakete iz requirements.txt:

    pip install -r requirements.txt


### 4. Pokrenite aplikaciju
Pokrenite aplikaciju koristeći uvicorn:

    uvicorn app.main:app --reload

### 5. Otvorite preglednik

Otvorite preglednik i posjetite:
http://localhost:8000 (ili http://127.0.0.1:8000/)









 
 
   






   

