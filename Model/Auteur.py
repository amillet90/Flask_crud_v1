import db


def insert(prenom, nom):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO Auteur VALUES (null, %s, %s)'
            cursor.execute(sql, (prenom, nom))

        connection.commit()
    finally:
        db.close_db()


def update(id, prenom, nom):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = ('UPDATE Auteur '
                   'SET prenomAuteur = %s, nomAuteur = %s '
                   'WHERE idAuteur = %s')
            cursor.execute(sql, (prenom, nom, id))

        connection.commit()
    finally:
        db.close_db()


def list():
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM Auteur'
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        db.close_db()


def get(id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM Auteur WHERE idAuteur = %s'
            cursor.execute(sql, (id))
            return cursor.fetchone()
    finally:
        db.close_db()


def delete(id):
    connection = db.get_db()

    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM Auteur WHERE idAuteur = %s'
            cursor.execute(sql, (id))

        connection.commit()
    finally:
        db.close_db()
