# Vaihe 2 – Ensimmäinen Flask-sovellus

Luodaan:
```text
elokuvasivusto/
├── .venv/
└── app.py
```
```python
app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Tervetuloa elokuvasivustolle!"


if __name__ == "__main__":
    app.run(debug=True)
```
Käynnistä sovellus:
```python
python app.py
```
Avaa selaimessa:
```text
http://127.0.0.1:5000
```
## Mitä tapahtuu?

Selain pyytää etusivua:

```text
Selain
   ↓
Flask
   ↓
@app.route("/")
   ↓
home()
   ↓
Vastaus selaimelle
```
## Opiskelijan tavoite

Opiskelija ymmärtää:

- mikä Flask on
- mikä reitti on
- miten selain ja Flask keskustelevat
- mitä debug=True tarkoittaa