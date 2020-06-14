import db


def insert(titre, date_parution, photo, prix, auteur_id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO Oeuvre VALUES (null, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (titre, date_parution, photo, prix, auteur_id))

        connection.commit()
    finally:
        db.close_db()


def update(id, titre, date_parution, photo, prix, auteur_id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = ('UPDATE Oeuvre '
                   'SET '
                   'titreOeuvre = %s, '
                   'dateParutionOeuvre = %s, '
                   'photoOeuvre = %s, '
                   'prixOeuvre = %s, '
                   'auteurIdOeuvre = %s '
                   'WHERE idOeuvre = %s')
            cursor.execute(sql, (titre, date_parution,
                                 photo, prix, auteur_id, id))

        connection.commit()
    finally:
        db.close_db()


def list():
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM Oeuvre'
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        db.close_db()


def find_by(auteur_id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM Oeuvre WHERE auteurIdOeuvre = %s'
            cursor.execute(sql, (auteur_id))
            return cursor.fetchall()
    finally:
        db.close_db()


def get(id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM Oeuvre WHERE idOeuvre = %s'
            cursor.execute(sql, (id))
            return cursor.fetchone()
    finally:
        db.close_db()


def delete(id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM Oeuvre WHERE idOeuvre = %s'
            cursor.execute(sql, (id))

        connection.commit()
    finally:
        db.close_db()
