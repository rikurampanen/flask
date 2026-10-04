# Vaihe 4 – Pythonista dataa HTML:ään

Nyt elokuvien nimet siirretään Pythonin käsiteltäväksi.

## app.py
```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    elokuvat = [
        "Inception",
        "The Dark Knight",
        "Interstellar"
    ]

    return render_template(
        "index.html",
        elokuvat=elokuvat
    )


if __name__ == "__main__":
    app.run(debug=True)
```

## templates/index.html

Korvaa aiemmat elokuvien `<p>`-elementit Jinja-silmukalla:
```html
<h2>Elokuvat</h2>

{% for elokuva in elokuvat %}

    <p>{{ elokuva }}</p>

{% endfor %}
```
## Mitä tässä tapahtuu?

Python antaa templaten käyttöön muuttujan:

`elokuvat`

Jinja käy listan läpi:
```text
Python
   ↓
elokuvat
   ↓
Jinja
   ↓
HTML
```

## Opiskelijan tavoite

Opiskelija oppii:

- miten data välitetään Pythonista templateen
- Jinja-syntaksin
- for-silmukan HTML:ssä