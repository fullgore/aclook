import os
import logging

from flask import Flask
from flask.logging import default_handler

from aclook import appSC

CONFIG_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
    'production': 'config.ProductionConfig',
}


def configure_loggers(app):
    loggers = app.config.get("LOGGERS")
    for logger_name, logger_value in loggers.items():
        root_logger = logging.getLogger(logger_name)
        root_logger.addHandler(default_handler)
        root_logger.setLevel(logger_value)


def register_services(app):
    appSC.bird_socket.provided_by(app.config['BIRD_SOCKET'])
    appSC.bird_timeout.provided_by(app.config['BIRD_TIMEOUT'])


def create_app():
    flask_env = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(CONFIG_MAPPER.get(flask_env, 'development'))

    configure_loggers(app)

    import aclook
    aclook.init_app(app)

    register_services(app)

    import modules
    modules.init_app(app)

    return app
