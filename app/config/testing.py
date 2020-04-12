import logging
from os import getenv


class BaseConfig:
    BIRD_SOCKET = getenv('BIRD_SOCKET', '/usr/local/run/bird.ctl')
    LOGGERS = {
        'aclook': logging.DEBUG,
        'utils.ACBird': logging.DEBUG,
        'utils.ACBirdParser': logging.DEBUG,
        'utils.ACBirdCommand': logging.DEBUG,
    }
