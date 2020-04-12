import logging
from os import getenv


class BaseConfig:
    BIRD_SOCKET = getenv('BIRD_SOCKET', '/usr/local/run/bird.ctl')
    LOGGERS = {
        'aclook': logging.WARN,
        'utils.ACBird': logging.WARN,
        'utils.ACBirdParser': logging.WARN,
        'utils.ACBirdCommand': logging.WARN,
    }
