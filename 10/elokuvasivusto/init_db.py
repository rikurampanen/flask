import sqlite3


conn = sqlite3.connect("elokuvat.db")


conn.execute("""
    CREATE TABLE IF NOT EXISTS elokuvat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nimi TEXT NOT NULL,
        vuosi INTEGER,
        genre TEXT,
        arvosana REAL,
        kuva TEXT
    )
""")


elokuvat = [
    (
        "Inception",
        2010,
        "Sci-fi",
        8.8,
        "inception.jpg"
    ),
    (
        "The Dark Knight",
        2008,
        "Toiminta",
        9.0,
        "dark_knight.jpg"
    ),
    (
        "Interstellar",
        2014,
        "Sci-fi",
        8.7,
        "interstellar.jpg"
    ),
    (
        "The Matrix",
        1999,
        "Sci-fi",
        8.7,
        "matrix.jpg"
    )
]


conn.executemany("""
    INSERT INTO elokuvat
    (nimi, vuosi, genre, arvosana, kuva)
    VALUES (?, ?, ?, ?, ?)
""", elokuvat)


conn.commit()
conn.close()


print("Tietokanta luotu ja elokuvat lisätty!")