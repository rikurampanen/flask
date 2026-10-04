# Vaihe 10 – SQLite-tietokanta

Tässä vaiheessa tehdään projektin ensimmäinen suuri rakenteellinen muutos.

Tähän asti:

```text
Python-lista
     ↓
   Flask
     ↓
   Jinja
     ↓
   HTML
```

Nyt:

```text
  SQLite
     ↓
   Flask
     ↓
   Jinja
     ↓
   HTML
```

HTML-sivujen ei tarvitse tietää, mistä data tulee.

Ne saavat edelleen muuttujan: `elokuvat`

Erona on vain se, että elokuvat tulevat nyt tietokannasta.

## Projektirakenne
```text
elokuvasivusto/
├── .venv/
├── app.py
├── init_db.py
├── elokuvat.db
├── static/
│   ├── style.css
│   └── images/
│       ├── inception.jpg
│       ├── dark_knight.jpg
│       ├── interstellar.jpg
│       └── matrix.jpg
└── templates/
    ├── index.html
    └── elokuva.html
```

Tietokannan alustaminen pidetään omassa tiedostossaan.

## init_db.py

Luo uusi tiedosto: `init_db.py`

**init_db.py**

```python
import sqlite3


conn = sqlite3.connect("elokuvat.db")


conn.execute("""
    CREATE TABLE IF NOT EXISTS elokuvat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nimi TEXT NOT NULL,
        vuosi INTEGER,
        genre TEXT,
        arvosana REAL,
        kuva TEXT
    )
""")


elokuvat = [
    (
        "Inception",
        2010,
        "Sci-fi",
        8.8,
        "inception.jpg"
    ),
    (
        "The Dark Knight",
        2008,
        "Toiminta",
        9.0,
        "dark_knight.jpg"
    ),
    (
        "Interstellar",
        2014,
        "Sci-fi",
        8.7,
        "interstellar.jpg"
    ),
    (
        "The Matrix",
        1999,
        "Sci-fi",
        8.7,
        "matrix.jpg"
    )
]


conn.executemany("""
    INSERT INTO elokuvat
    (nimi, vuosi, genre, arvosana, kuva)
    VALUES (?, ?, ?, ?, ?)
""", elokuvat)


conn.commit()
conn.close()


print("Tietokanta luotu ja elokuvat lisätty!")
```

## Tietokannan luominen

Aja:

```bash
python init_db.py
```

Projektikansioon syntyy: `elokuvat.db`

## Mitä init_db.py tekee?

Se:

1. avaa SQLite-tietokannan
2. luo elokuvat-taulun
3. lisää siihen valmiiksi neljä elokuvaa
4. tallentaa muutokset
5. sulkee yhteyden

> app.py:n ei tarvitse luoda tietokantaa.

**Tärkeä huomio**

`init_db.py` on tarkoitettu tietokannan alustamiseen. Sitä ei suoriteta jokaisella Flask-sovelluksen käynnistyskerralla.

Jos sen suorittaa uudelleen nykyisellä koodilla, samat elokuvat lisätään uudestaan.

Tämä voidaan myöhemmin korjata esimerkiksi tarkistamalla, onko taulussa jo tietoja.

## SQLite-yhteys app.py:ssä

Poistetaan Python-lista app.py:stä.

**Lisätään SQLite:**

```python
import sqlite3

# Tehdään yhteysfunktio:

def get_db_connection():

    conn = sqlite3.connect("elokuvat.db")
    conn.row_factory = sqlite3.Row

    return conn
```

`row_factory` mahdollistaa tietojen käyttämisen esimerkiksi näin: `elokuva["nimi"]`

## Etusivu hakee elokuvat tietokannasta

**app.py:**
```python
@app.route("/")
def home():

    conn = get_db_connection()

    elokuvat = conn.execute(
        "SELECT * FROM elokuvat"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        elokuvat=elokuvat
    )
```

Tässä:

```sql
SELECT * FROM elokuvat
```

hakee kaikki elokuvat tietokannasta.

Sitten ne annetaan templaten käyttöön: `elokuvat=elokuvat`

Tämän ansiosta nykyinen Jinja-koodi voi jatkaa toimintaansa lähes sellaisenaan.

## Yksittäinen elokuva tietokannasta

Aiemmin reitti käytti elokuvan nimeä: `/elokuva/Inception`

Tietokannan kanssa käytetään id:tä: `/elokuva/1`

**Reitti:**

```python
@app.route("/elokuva/<int:id>")
def elokuva(id):

    conn = get_db_connection()

    elokuva = conn.execute(
        "SELECT * FROM elokuvat WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if elokuva is None:
        return "Elokuvaa ei löytynyt"

    return render_template(
        "elokuva.html",
        elokuva=elokuva
    )
```

## Miksi id?

Tietokanta antaa jokaiselle elokuvalle yksilöllisen tunnisteen:

```text
1 = Inception
2 = The Dark Knight
3 = Interstellar
4 = The Matrix
```

Tällöin URL:t ovat esimerkiksi:

```text
/elokuva/1
/elokuva/2
/elokuva/3
```

## Päivitetään linkki

Koska käytämme nyt id:tä, index.html:ssä:

```html
<a href="/elokuva/{{ elokuva.id }}">
    {{ elokuva.nimi }}
</a>
```

## Lopullinen app.py

```python
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():

    conn = sqlite3.connect("elokuvat.db")
    conn.row_factory = sqlite3.Row

    return conn


@app.route("/")
def home():

    conn = get_db_connection()

    elokuvat = conn.execute(
        "SELECT * FROM elokuvat"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        elokuvat=elokuvat
    )


@app.route("/elokuva/<int:id>")
def elokuva(id):

    conn = get_db_connection()

    elokuva = conn.execute(
        "SELECT * FROM elokuvat WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if elokuva is None:
        return "Elokuvaa ei löytynyt"

    return render_template(
        "elokuva.html",
        elokuva=elokuva
    )


if __name__ == "__main__":
    app.run(debug=True)
```