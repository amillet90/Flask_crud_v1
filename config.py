# Flask configuration
# -------------------

SECRET_KEY = 'THISISAREALLYBADSECRETKEY'

# Database Configuration
# ----------------------

MYSQL_HOSTNAME = 'localhost'
MYSQL_DATABASE = 'flask_app'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'password'

# Logging configuration
# ---------------------

LOGGER_CONFIGURATION = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}
