import logging
from logging import config
from pathlib import Path
import os
import time
from logging.handlers import RotatingFileHandler

import flask
from flask import request, g, current_app
from app.logging_config.log_formatters import RequestFormatter
log_con = flask.Blueprint('log_con', __name__)


@log_con.before_app_request
def before_request_logging():
    request_logger = logging.getLogger('requests')
    request_logger.info("Before Request")


@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    request_logger = logging.getLogger('requests')
    request_logger.info("After Request")

    return response


@log_con.before_app_first_request
def configure_logging():
    log_config_dir = Path(__file__).parent
    config.fileConfig(log_config_dir / "logging.cfg")
    log = logging.getLogger("root")
    log.info("My App Logger")
    log = logging.getLogger("errors")
    log.info("THis broke")




LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'RequestFormatter': {
            '()': 'app.logging_config.log_formatters.RequestFormatter',
            'format': '[%(asctime)s] [%(process)d] %(remote_addr)s requested %(url)s'
                        '%(levelname)s in %(module)s: %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/normal.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.request': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/request.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.custom': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'RequestFormatter',
            'filename': 'app/logs/custom.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/errors.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default','file.handler', 'file.handler.request'],
            'level': 'DEBUG',
            'propagate': True
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default','file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'werkzeug': {  # if __name__ == '__main__'
            'handlers': ['file.handler.custom'],
            'level': 'DEBUG',
            'propagate': False
        },
        'myApp': {  # if __name__ == '__main__'
            'handlers': ['file.handler.custom'],
            'level': 'DEBUG',
            'propagate': False
        },
        'myerrors': {  # if __name__ == '__main__'
            'handlers': ['file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },

    }
}
