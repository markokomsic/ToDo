# ToDo Web Aplikacija

Ovo je jednostavna ToDo web aplikacija izgrađena s FastAPI, SQLite i Jinja2 templatingom. Aplikacija podržava registraciju korisnika, prijavu te CRUD operacije za upravljanje zadacima.

## Značajke

- Registracija i prijava korisnika
- Autentifikacija temeljem JWT-a
- Kreiranje, čitanje, ažuriranje i brisanje (CRUD) zadataka
- Jinja2 templating za prikaz HTML stranica

## Opis Fajlova
- app/main.py: Ulazna točka za FastAPI aplikaciju.
- app/models.py: Definicija SQLAlchemy modela za korisnike i zadatke.
- app/schemas.py: Pydantic modeli za validaciju podataka.
- app/crud.py: Funkcije za CRUD operacije nad bazom podataka.
- app/database.py: Konfiguracija za bazu podataka.
- app/auth.py: Funkcije za generiranje i provjeru JWT tokena.
- app/routers/todos.py: Rute za upravljanje zadacima.
- app/routers/users.py: Rute za registraciju i prijavu korisnika.
- templates/: Direktorij sa HTML šablonima.
