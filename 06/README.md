# Vaihe 6 – Jokaiselle elokuvalle oma sivu

Nyt tehdään jokaiselle elokuvalle oma sivu.

Esimerkiksi:

`/elokuva/Inception`

## Elokuvalista yhteen paikkaan

Tässä vaiheessa elokuvalista siirretään app.py:ssä moduulin tasolle, jotta sekä etusivu että yksittäisen elokuvan reitti voivat käyttää samaa listaa.

## app.py

```python
from flask import Flask, render_template

app = Flask(__name__)


elokuvat = [
    {
        "nimi": "Inception",
        "vuosi": 2010,
        "genre": "Sci-fi",
        "arvosana": 8.8
    },
    {
        "nimi": "The Dark Knight",
        "vuosi": 2008,
        "genre": "Toiminta",
        "arvosana": 9.0
    },
    {
        "nimi": "Interstellar",
        "vuosi": 2014,
        "genre": "Sci-fi",
        "arvosana": 8.7
    }
]


@app.route("/")
def home():

    return render_template(
        "index.html",
        elokuvat=elokuvat
    )


@app.route("/elokuva/<nimi>")
def elokuva(nimi):

    for elokuva in elokuvat:

        if elokuva["nimi"] == nimi:

            return render_template(
                "elokuva.html",
                elokuva=elokuva
            )

    return "Elokuvaa ei löytynyt"


if __name__ == "__main__":
    app.run(debug=True)
```

## Uusi template

Luodaan:

```text
templates/
├── index.html
└── elokuva.html
```

## templates/elokuva.html

```html
<!DOCTYPE html>
<html lang="fi">

<head>
    <meta charset="UTF-8">
    <title>{{ elokuva.nimi }}</title>
</head>

<body>

    <h1>{{ elokuva.nimi }}</h1>

    <p>Julkaisuvuosi: {{ elokuva.vuosi }}</p>

    <p>Genre: {{ elokuva.genre }}</p>

    <p>Arvosana: {{ elokuva.arvosana }}</p>

    <a href="/">← Takaisin elokuviin</a>

</body>

</html>
```

Etusivun linkki

## index.html:

```html
<h3>
    <a href="/elokuva/{{ elokuva.nimi }}">
        {{ elokuva.nimi }}
    </a>
</h3>
```

Nyt opiskelija voi klikata elokuvan nimeä ja siirtyä sen omalle sivulle.

## Opiskelijan tavoite

Opiskelija oppii:

- dynaamisen reitin
- URL-parametrin
- tietyn tietueen etsimisen
- uuden templaten käyttämisen
- linkittämisen Flask-reittiin