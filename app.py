import os
from logging.config import dictConfig

from flask import Flask

import config


def load_logging_config(app):
    dictConfig(app.config['LOGGER_CONFIGURATION'])


def make_instance_path(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def load_all_controllers(app):
    from Controller import AuteurController, OeuvreController, MainController

    controllers = [AuteurController.c, OeuvreController.bp, MainController.c]
    for c in controllers:
        app.register_blueprint(c)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    load_logging_config(app)
    make_instance_path(app)

    load_all_controllers(app)

    return app


if __name__ == '__main__':
    print("Run this application with 'flask run'.")
