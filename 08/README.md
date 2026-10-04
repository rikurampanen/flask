# Vaihe 8 – CSS ja elokuvakortit

Nyt sovelluksen toiminnallisuus toimii. Seuraavaksi tehdään ulkoasu.

## Luodaan:

```text
static/
└── style.css
```

Projektirakenne:

```text
elokuvasivusto/
├── .venv/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── elokuva.html
```

## static/style.css

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    background-color: #f2f2f2;
}

header {
    background-color: #222;
    color: white;
    padding: 20px;
}

header h1 {
    margin: 0;
}

main {
    max-width: 1000px;
    margin: 30px auto;
    padding: 0 20px;
}

.elokuvat {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.elokuva {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
}

.elokuva h3 {
    margin-top: 0;
}

.elokuva a {
    color: #222;
    text-decoration: none;
}

.elokuva a:hover {
    text-decoration: underline;
}
```

## CSS:n yhdistäminen HTML:ään

Lisää index.html:n `<head>`-osaan:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

## Elokuvakortit

Muuta elokuvien näyttäminen seuraavanlaiseksi:

```html
<div class="elokuvat">

    {% for elokuva in elokuvat %}

        <div class="elokuva">

            <h3>
                <a href="/elokuva/{{ elokuva.nimi }}">
                    {{ elokuva.nimi }}
                </a>
            </h3>

            <p>{{ elokuva.vuosi }}</p>

            <p>{{ elokuva.genre }}</p>

            <p>⭐ {{ elokuva.arvosana }}</p>

        </div>

    {% endfor %}

</div>
```

## Opiskelijan tavoite

Opiskelija oppii:

- static-kansion
- CSS:n yhdistämisen Flaskiin
- url_for()-funktion
- HTML:n ja CSS:n eron