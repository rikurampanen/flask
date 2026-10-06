# Flask-elokuvasivusto

Tässä repositoryssa rakennetaan Flaskilla elokuvasivusto vaihe vaiheelta.

Harjoituksen tarkoituksena on oppia Flask-verkkosovelluksen perusteet käytännön projektin avulla. Sovellusta kehitetään pienissä vaiheissa siten, että jokainen vaihe rakentuu edellisen vaiheen päälle.

Alussa elokuvat ovat Python-koodissa. Lopussa elokuvat haetaan SQLite-tietokannasta.

## Tavoite

Projektin aikana opitaan muun muassa:

- Pythonin ja Flaskin perusteet
- Flask-reitit
- HTML-templatet
- Jinja-templatekieli
- datan välittäminen Pythonista HTML:ään
- dynaamiset URL-osoitteet
- staattiset tiedostot
- CSS
- kuvien käyttäminen verkkosivulla
- SQLite-tietokannan perusteet
- SQL-kyselyt Flask-sovelluksessa

Lopputuloksena on elokuvasivusto, jossa elokuvia voidaan näyttää tietokannasta ja jokaisella elokuvalla on oma sivunsa.

# Repositoryn rakenne

Jokainen opetuksen vaihe sijaitsee omassa kansiossaan:

```text
.
├── 01/
├── 02/
├── 03/
├── 04/
├── 05/
├── 06/
├── 07/
├── 08/
├── 09/
└── 10/
```

Jokainen kansio sisältää:

1. kyseiseen vaiheeseen asti rakennetun toimivan version sovelluksesta
2. kyseisen vaiheen `README.md`-tiedoston
3. kaikki tarvittavat tiedostot, jotta kyseinen vaihe voidaan käynnistää

Esimerkiksi:

```text
01/
├── README.md
└── app.py
```

Seuraavassa vaiheessa mukana ovat kaikki siihen mennessä tarvittavat tiedostot:
```text
03/
├── README.md
├── app.py
└── templates/
    └── index.html
```

Myöhemmissä vaiheissa rakenne kasvaa:

```text
10/
├── README.md
├── app.py
├── init_db.py
├── elokuvat.db
├── static/
│   ├── style.css
│   └── images/
└── templates/
    ├── index.html
    └── elokuva.html
```

Näin jokainen vaihe on itsenäisesti tarkasteltavissa.

# Vaiheiden eteneminen

## 01 – Projektin perustaminen

Ensimmäisessä vaiheessa luodaan Flask-projekti ja Pythonin virtuaaliympäristö.

Opitaan:

- projektikansion luominen
- virtuaaliympäristö
- Flaskin asentaminen

Projektissa on tässä vaiheessa ensimmäiset Flask-projektin tarvitsemat tiedostot.

**[Siirry vaiheeseen 01](01/README.md)**

## 02 – Ensimmäinen Flask-sovellus

Tehdään ensimmäinen toimiva Flask-sovellus.

Opitaan:

- Flask-sovelluksen luominen
- reitti
- funktion käyttäminen reittinä
- Flask-palvelimen käynnistäminen

Sovellus palauttaa ensimmäisen tekstivastauksen selaimelle.

**[Siirry vaiheeseen 02](02/README.md)**

## 03 – HTML-template

Pythonista palautettava teksti korvataan oikealla HTML-sivulla.

Opitaan:

- templates-kansio
- HTML-tiedosto
- render_template()
- Pythonin ja HTML erottaminen toisistaan

**[Siirry vaiheeseen 03](03/README.md)**

## 04 – Python-data HTML:ään

Elokuvat siirretään Python-listaan ja näytetään Jinja-templatessa.

Opitaan:

- Python-lista
- datan välittäminen templaten käyttöön
- Jinja-muuttujat
- Jinja for-silmukka

Tässä vaiheessa samaa HTML-rakennetta voidaan käyttää usean elokuvan näyttämiseen.

**[Siirry vaiheeseen 04](04/README.md)**

## 05 – Rakenteiset elokuvat

Pelkkien nimien sijaan elokuvat muutetaan rakenteisiksi tietueiksi.

Elokuvalla on esimerkiksi:

- nimi
- julkaisuvuosi
- genre
- arvosana

Opitaan:

- Pythonin sanakirjat
- rakenteisen datan käsittely
- useiden tietojen näyttäminen Jinjalla

Tämä rakenne valmistaa opiskelijaa myöhemmin SQLite-tietokantaan.

**[Siirry vaiheeseen 05](05/README.md)**

## 06 – Yksittäinen elokuvasivu

Jokaiselle elokuvalle tehdään oma sivu.

Esimerkiksi:

`/elokuva/Inception`

Opitaan:

- dynaaminen Flask-reitti
- URL-parametri
- tietyn elokuvan etsiminen
- uuden templaten käyttäminen
- sivujen väliset linkit

**[Siirry vaiheeseen 06](06/README.md)**

## 07 – Elokuville yksilöllinen tunniste

Jokaiselle elokuvalle lisätään yksilöllinen id.

Aikaisemmin yksittäinen elokuva haettiin nimen perusteella. Nyt elokuva haetaan sen tunnisteen avulla:

```text
/elokuva/1
/elokuva/2
/elokuva/3
```

Samalla tutustutaan siihen, miten Flaskin dynaamisessa reitissä voidaan käyttää kokonaislukua:

```python
@app.route("/elokuva/<int:id>")
```

Tämä valmistaa sovellusta myöhempää SQLite-tietokantaa varten, jossa jokaisella elokuvalla on niin ikään oma id.#

**[Siirry vaiheeseen 07](07/README.md)**

## 08 – CSS ja elokuvakortit

Sivustolle rakennetaan visuaalinen ulkoasu.

Opitaan:

- static-kansio
- CSS
- Flaskin url_for()
- CSS-luokat
- elokuvakorttien rakentaminen
- CSS Grid

Elokuvat näytetään selkeinä kortteina.

**[Siirry vaiheeseen 08](08/README.md)**

## 09 – Elokuvien kuvat

Elokuvakortteihin ja yksittäisten elokuvien sivuille lisätään kuvat.

Opitaan:

- kuvien sijoittaminen static/images-kansioon
- kuvien käyttäminen HTMLä
- kuvan nimen tallentaminen osaksi elokuvan dataa
- Jinja ja dynaamiset kuvat

Tässä vaiheessa opiskelijoilla on myös mahdollisuus kokeilla omien tietojen lisäämistä elokuviin.

**[Siirry vaiheeseen 09](09/README.md)**

## 10 – SQLite-tietokanta

Viimeisessä vaiheessa elokuvadatan lähde muutetaan Python-listasta SQLite-tietokannaksi.

Aiemmin:

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

Opitaan:

- SQLite
- tietokannan luominen
- taulu
- sarakkeet
- rivit
- SELECT
- WHERE
- INSERT
- tietokantayhteyden muodostaminen
- tietokannasta tietojen hakeminen Flaskissa

Tietokannan alustaminen tehdään erillisessä tiedostossa:

`init_db.py`

Flask-sovellus säilyy tiedostossa:

`app.py`

Tarkoituksena on pitää tietokannan luonti ja Flask-sovelluksen toiminta erillään.

**[Siirry vaiheeseen 10](10/README.md)**

# Vaiheiden tärkeä periaate

Jokainen vaihe sisältää valmiin version sovelluksesta kyseiseen vaiheeseen asti.

Esimerkiksi:

`01/`

sisältää vaiheen 1 version.

`05/`

sisältää kaiken, mitä sovelluksessa on tehty vaiheeseen 5 mennessä.

`10/`

sisältää lopullisen version, jossa SQLite on käytössä.

Näin opiskelija voi aina:

1. tarkastella nykyistä vaihetta
2. verrata omaa koodiaan malliin
3. palata aiempaan vaiheeseen
4. aloittaa harjoituksen uudelleen tietystä vaiheesta

# Suositeltu työskentelytapa

Opiskelijan ei tarvitse aloittaa suoraan kansiosta 10.

Suositeltu etenemisjärjestys on:

`01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10`

Jokaisen vaiheen jälkeen sovellus kannattaa käynnistää ja testata ennen seuraavaan vaiheeseen siirtymistä.

Esimerkiksi:

```bash
cd 01
python app.py
```

Seuraavassa vaiheessa:

```bash
cd ../02
python app.py
```

ja niin edelleen.

# Projektin arkkitehtuuri lopussa

Vaiheen 10 jälkeen sovelluksen kokonaisrakenne on:

```text
                    Selain
                       │
                       ▼
                    Flask
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
          Reitit              SQLite
             │                   │
             └─────────┬─────────┘
                       ▼
                    Jinja
                       │
                       ▼
                      HTML
                       │
                       ▼
                      CSS
```

Kuvat sijaitsevat `static/images`-kansiossa.

Tietokannan alustamisesta vastaa `init_db.py`.

Flask-sovelluksesta vastaa `app.py`.

# Projektin lopullinen rakenne

Vaiheessa 10 projektin rakenne on suunnilleen:
```text
10/
├── README.md
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

# Teknologiat

Projektissa käytetään:

- Python
- Flask
- Jinja
- HTML
- CSS
- SQLite

Erillisiä tietokantakirjastoja ei tarvita, sillä Python sisältää sqlite3-moduulin.

# Opetuksen tavoite

Tämän repositoryn tärkein tavoite ei ole rakentaa mahdollisimman monimutkaista elokuvasivustoa.

Tavoitteena on ymmärtää, miten verkkosovellus kehittyy askel kerrallaan:

```text
Ensimmäinen Flask-reitti
        ↓
    HTML-sivu
        ↓
    Python-data
        ↓
      Jinja
        ↓
    Dynaamiset sivut
        ↓
       CSS
        ↓
      Kuvat
        ↓
      SQLite
```

Kun nämä perusasiat ovat tuttuja, sovellukseen voidaan myöhemmin lisätä uusia ominaisuuksia, kuten:

- uuden elokuvan lisääminen lomakkeella
- elokuvan muokkaaminen
- elokuvan poistaminen
- elokuvien hakeminen
- lajittelu
- genren perusteella suodattaminen
- käyttäjät
- kirjautuminen
- arvostelut

Nämä ominaisuudet eivät kuulu tämän kymmenen vaiheen perusharjoitukseen, vaan niitä voidaan käyttää jatkoharjoituksina.

# Opiskelijalle

Jos olet tekemässä harjoitusta ensimmäistä kertaa, aloita kansiosta:

`01/`

Lue ensin sen `README.md` ja tee vaihe loppuun.

Siirry vasta sen jälkeen kansioon:

`02/`

Jatka samalla tavalla aina vaiheeseen `10` asti.

Älä kopioi seuraavan vaiheen koodia etukäteen. Harjoituksen idea on, että sovellus rakennetaan vähitellen ja jokainen uusi käsite perustuu aiemmin opittuun.

Hyvä tavoite on saada jokainen vaihe toimimaan ennen seuraavaan siirtymistä.

# Lisenssi

Tämä kurssi on julkaistu [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) -lisenssillä.

Copyright © Riku Rampanen