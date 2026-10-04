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