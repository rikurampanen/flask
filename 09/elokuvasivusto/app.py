from flask import Flask, render_template

app = Flask(__name__)


elokuvat = [
    {
        "nimi": "Inception",
        "vuosi": 2010,
        "genre": "Sci-fi",
        "arvosana": 8.8,
        "kuva": "inception.jpg"
    },
    {
        "nimi": "The Dark Knight",
        "vuosi": 2008,
        "genre": "Toiminta",
        "arvosana": 9.0,
        "kuva": "dark_knight.jpg"
    },
    {
        "nimi": "Interstellar",
        "vuosi": 2014,
        "genre": "Sci-fi",
        "arvosana": 8.7,
        "kuva": "interstellar.jpg"
    },
    {
        "nimi": "The Matrix",
        "vuosi": 1999,
        "genre": "Sci-fi",
        "arvosana": 8.7,
        "kuva": "matrix.jpg"
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