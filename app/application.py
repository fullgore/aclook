import os
import logging

from flask import Flask

from aclook import appSC


def configure_loggers(app):
    loggers = app.config.get("LOGGERS")
    for logger_name, logger_value in loggers.items():
        logging.getLogger(logger_name).setLevel(logger_value)


def register_services(app):
    appSC.bird_socket.provided_by(app.config['BIRD_SOCKET'])


def create_app():
    flask_env = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)

    app.config.from_object(f'config.{flask_env}.BaseConfig')

    configure_loggers(app)

    import aclook
    aclook.init_app(app)

    register_services(app)

    import modules
    modules.init_app(app)

    return app
