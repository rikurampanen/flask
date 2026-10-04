# Vaihe 5 – Elokuvista sanakirjoja

Pelkkä elokuvan nimi ei vielä riitä.

Jokaisella elokuvalla voi olla esimerkiksi:

- nimi
- julkaisuvuosi
- genre
- arvosana

## app.py

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

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

    return render_template(
        "index.html",
        elokuvat=elokuvat
    )


if __name__ == "__main__":
    app.run(debug=True)
```

## templates/index.html

```html
<h2>Elokuvat</h2>

{% for elokuva in elokuvat %}

    <h3>{{ elokuva.nimi }}</h3>

    <p>Julkaisuvuosi: {{ elokuva.vuosi }}</p>

    <p>Genre: {{ elokuva.genre }}</p>

    <p>Arvosana: {{ elokuva.arvosana }}</p>

    <hr>

{% endfor %}
```

## Opiskelijan tavoite

Opiskelija oppii rakenteisen datan käsittelyn.

Tämä valmistaa myöhemmin tietokannan käyttämiseen, koska tietokannan sarakkeet vastaavat hyvin pitkälti näitä tietoja.