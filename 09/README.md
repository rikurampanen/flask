# Vaihe 9 – Elokuvien kuvat

Nyt lisätään elokuville kuvat.

```text
Projektirakenne
elokuvasivusto/
├── .venv/
├── app.py
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

## Elokuvan dataan kuva

Lisätään jokaiseen elokuvaan kuva.

Esimerkiksi The Dark Knight:
```python
{
    "nimi": "The Dark Knight",
    "vuosi": 2008,
    "genre": "Toiminta",
    "arvosana": 9.0,
    "kuva": "dark_knight.jpg"
}
```

## Kuva HTML:ään

Lisää elokuvakorttiin:

```html
<img src="{{ url_for('static', filename='images/' + elokuva.kuva) }}" alt="{{ elokuva.nimi }}">
```

## CSS

Lisää style.css:ään:

```css
.elokuva img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
}
```

Sama kuva voidaan näyttää myös elokuva.html:ssä:

```html
<img src="{{ url_for('static', filename='images/' + elokuva.kuva) }}" alt="{{ elokuva.nimi }}">
```

## Opiskelijan tavoite

Opiskelija oppii, miten:

- kuvat sijoitetaan Flask-projektissa
- staattisia tiedostoja käytetään
- Python/Jinja-data vaikuttaa HTML:ään
- samaa dataa voidaan käyttää usealla sivulla

## Harjoitus

Opiskelijat voivat itse lisätä uusia tietoja elokuviin.

Esimerkiksi opiskelija voi lisätä elokuvan sanakirjaan uuden kentän ja näyttää sen HTML-sivulla.