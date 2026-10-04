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