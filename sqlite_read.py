# SQLITE: LECTURE DE LA TABLE

import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

# curseur.execute("SELECT * FROM artiste")
# curseur.execute("SELECT nom FROM artiste")
# artistes = curseur.fetchall()
# print(artistes)

# for artiste in artistes:
#     print(artiste[1])

# for artiste in curseur.execute("SELECT * FROM artiste"):
#     print(artiste)

# albums_dms = curseur.execute(
#     'SELECT titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id AND ar.nom = "DAMSO"').fetchall()

# print(albums_dms)

nom_titre = curseur.execute(
    """SELECT nom, titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id""").fetchall()
print(nom_titre)


connexion.close()
