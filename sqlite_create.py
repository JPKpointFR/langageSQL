# SQLITE: CREATION DE LA TABLE
import sqlite3

# connexion = "albums2.db"
# executer / curseur
# commit
# fermer

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")

curseur.execute("""CREATE TABLE album (album_id INTEGER NOT NULL PRIMARY KEY,
    artiste_id INTEGER REFERENCES artiste, 
    titre VARCHAR,
    annee_sortie INTEGER);""")

curseur.execute(
    """INSERT INTO artiste (nom) VALUES ("Michael Jackson");""")  # 1
mj_id = curseur.lastrowid
curseur.execute("""INSERT INTO artiste (nom) VALUES ("DAMSO");""")  # 1
damso_id = curseur.lastrowid
curseur.execute(
    f"""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({mj_id}, "Thriller", 1982);""")

curseur.execute(
    f"""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({damso_id}, "QALF", 2020);""")
curseur.execute(
    f"""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({damso_id}, "QALF INFINITY", 2021);""")

connexion.commit()
connexion.close()
