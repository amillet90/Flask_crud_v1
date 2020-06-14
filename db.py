from flask import current_app, g
import pymysql


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=current_app.config['MYSQL_HOSTNAME'],
            user=current_app.config['MYSQL_USERNAME'],
            password=current_app.config['MYSQL_PASSWORD'],
            db=current_app.config['MYSQL_DATABASE'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
