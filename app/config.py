import logging
from os import getenv


class BaseConfig:
    DEBUG = False
    BIRD_SOCKET = getenv('BIRD_SOCKET', '/usr/local/run/bird.ctl')
    BIRD_TIMEOUT = 15.
    LOGGERS = {
        'aclook': logging.WARN,
        'utils.ACBird': logging.WARN,
        'utils.ACBirdParser': logging.WARN,
        'utils.ACBirdCommand': logging.WARN,
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOGGERS = {
        'aclook': logging.DEBUG,
        'utils.ACBird': logging.DEBUG,
        'utils.ACBirdParser': logging.DEBUG,
        'utils.ACBirdCommand': logging.DEBUG,
    }


class TestingConfig(BaseConfig):
    DEBUG = True
    BIRD_TIMEOUT = 5.


class ProductionConfig(BaseConfig):
    BIRD_TIMEOUT = 7.
