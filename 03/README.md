# Vaihe 3 – HTML-template

Pelkkä Pythonista palautettava teksti ei riitä oikeaan verkkosivuun.

## Luodaan templates-kansio:
```text
elokuvasivusto/
├── .venv/
├── app.py
└── templates/
    └── index.html
```
## templates/index.html
```html
<!DOCTYPE html>
<html lang="fi">

<head>
    <meta charset="UTF-8">
    <title>Elokuvasivusto</title>
</head>

<body>

    <h1>Elokuvasivusto</h1>

    <p>Tervetuloa elokuvien maailmaan!</p>

    <h2>Suositellut elokuvat</h2>

    <p>Inception</p>
    <p>The Dark Knight</p>
    <p>Interstellar</p>

</body>

</html>
```
## Muokataan app.py:
```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
```
## Opiskelijan tavoite

Opiskelija oppii:

- templates-kansion tarkoituksen
- HTML:n ja Pythonin eron
- render_template()-funktion