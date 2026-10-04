# Vaihe 7 – Datan pitäminen yhdessä paikassa

Vaiheessa 6 elokuvalista siirrettiin yhteen paikkaan.

Nyt lisätään neljäs elokuva:

```python
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
    },
    {
        "nimi": "The Matrix",
        "vuosi": 1999,
        "genre": "Sci-fi",
        "arvosana": 8.7
    }
]
```

Tärkeä ajatus on, että sama elokuvat-lista toimii kaikkialla sovelluksessa.

```text
                    elokuvat
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
         etusivu            elokuvasivu
```

## Opiskelijan tavoite

Opiskelija ymmärtää, miksi samaa dataa ei kannata kopioida useaan paikkaan.

Tämä toimii samalla johdatuksena seuraavaan vaiheeseen: data kannattaa pitää erillään käyttöliittymästä.