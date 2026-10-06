# Vaihe 7 – Elokuville yksilöllinen tunniste

Vaiheessa 6 jokaiselle elokuvalle tehtiin oma sivu.

Elokuva löytyi sen nimen perusteella:

`/elokuva/Inception`

Tässä vaiheessa annetaan jokaiselle elokuvalle oma yksilöllinen tunniste eli id.

Esimerkiksi:
```text
1 = Inception
2 = The Dark Knight
3 = Interstellar
4 = The Matrix
```

Yksittäinen elokuva voidaan tämän jälkeen avata tunnisteen avulla:

`/elokuva/1`

## Miksi tarvitsemme tunnisteen?

Elokuvan nimi ei ole hyvä tunniste.

Nimi voi esimerkiksi muuttua tai kahdella tietueella voisi teoriassa olla sama nimi.

Tietokannoissa tietueille annetaan yleensä yksilöllinen tunniste.

Tässä vaiheessa teemme saman asian itse Pythonissa.

## Elokuvadatan muuttaminen

Lisätään jokaiselle elokuvalle id:

```python
elokuvat = [
    {
        "id": 1,
        "nimi": "Inception",
        "vuosi": 2010,
        "genre": "Sci-fi",
        "arvosana": 8.8
    },
    {
        "id": 2,
        "nimi": "The Dark Knight",
        "vuosi": 2008,
        "genre": "Toiminta",
        "arvosana": 9.0
    },
    {
        "id": 3,
        "nimi": "Interstellar",
        "vuosi": 2014,
        "genre": "Sci-fi",
        "arvosana": 8.7
    },
    {
        "id": 4,
        "nimi": "The Matrix",
        "vuosi": 1999,
        "genre": "Sci-fi",
        "arvosana": 8.7
    }
]
```

Nyt jokaisella elokuvalla on oma tunnisteensa.

## Reitin muuttaminen

Aikaisemmin reitti oli:

```python
@app.route("/elokuva/<nimi>")
def elokuva(nimi):
```

Nyt käytetään kokonaislukua:

```python
@app.route("/elokuva/<int:id>")
def elokuva(id):

<int:id> tarkoittaa, että Flask odottaa URL-osoitteeseen kokonaislukua.
```

Esimerkiksi: `/elokuva/1` välittää reitille arvon `id = 1`

## Elokuvan etsiminen

Aikaisemmin elokuvaa etsittiin nimen perusteella:

```python
for elokuva in elokuvat:

    if elokuva["nimi"] == nimi:

Nyt etsitään id perusteella:

for elokuva in elokuvat:

    if elokuva["id"] == id:
```

Näin sovellus löytää oikean elokuvan sen yksilöllisen tunnisteen avulla.

## Linkin muuttaminen

Myös etusivun linkki muutetaan käyttämään idä.

Aikaisemmin:

```html
<a href="/elokuva/{{ elokuva.nimi }}">
    {{ elokuva.nimi }}
</a>
```

Nyt:

```html
<a href="/elokuva/{{ elokuva.id }}">
    {{ elokuva.nimi }}
</a>
```
Esimerkiksi Inceptionin linkistä tulee:

`/elokuva/1`

## Koko sovelluksen rakenne

Tässä vaiheessa sovelluksen rakenne on:

```text
                    elokuvat
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
         etusivu            elokuvasivu
             │                   │
             └────── id ─────────┘
```

`id` toimii siis yhteisenä tunnisteena, jonka avulla tietty elokuva voidaan löytää.

## Miksi tämä on tärkeää myöhemmin?

Seuraavissa vaiheissa elokuvien ulkoasua kehitetään edelleen, mutta id säilyy osana elokuvadataa.

Lopulta elokuvat siirretään SQLite-tietokantaan.

Myös SQLite antaa jokaiselle elokuvalle oman id.

Silloin sovelluksen perusidea ei muutu:

**Vaihe 07:**

```text
Python-lista
    ↓
   id
    ↓
   Flask
    ↓
   HTML
```

ja myöhemmin:

**Vaihe 10:**

```text
SQLite
    ↓
   id
    ↓
   Flask
    ↓
   HTML
```

Tietolähde muuttuu, mutta elokuvan yksilöllinen tunniste säilyy.

Tämä tekee siirtymisestä tietokantaan huomattavasti helpompaa.