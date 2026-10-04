from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():

    conn = sqlite3.connect("elokuvat.db")
    conn.row_factory = sqlite3.Row

    return conn


@app.route("/")
def home():

    conn = get_db_connection()

    elokuvat = conn.execute(
        "SELECT * FROM elokuvat"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        elokuvat=elokuvat
    )


@app.route("/elokuva/<int:id>")
def elokuva(id):

    conn = get_db_connection()

    elokuva = conn.execute(
        "SELECT * FROM elokuvat WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if elokuva is None:
        return "Elokuvaa ei löytynyt"

    return render_template(
        "elokuva.html",
        elokuva=elokuva
    )


if __name__ == "__main__":
    app.run(debug=True)