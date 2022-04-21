import logging
from logging import config
from pathlib import Path

import flask
from flask import request, has_request_context
from app.logging_config.log_formatters import RequestFormatter
from logging.config import dictConfig

log_con = flask.Blueprint('log_con', __name__)

request_logger = logging.getLogger("requests")
errors_logger = logging.getLogger("errors")


def log_current_req():
    if has_request_context():
        request_logger.info(
            f'URL: {request.url} , Remote Address: {request.remote_addr} , '
            f'Request Method: {request.method}, Request Path: {request.path}, '
            f'IP: {request.headers.get("X-Forwarded-For", request.remote_addr)}, '
            f'Host: {request.host.split(":", 1)[0]}'
        )
    else:
        raise RuntimeError("No current request being processed")


@log_con.before_app_request
def before_request_logging():
    request_logger.info("Before Request")
    log_current_req()


@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    request_logger.info("After Request")

    return response


@log_con.before_app_first_request
def configure_logging():
    log_config_dir = Path(__file__).parent
    config.fileConfig(log_config_dir / "logging.cfg")

    # log = logging.getLogger("root")
    # log.info("My App Logger")
    try:
        1 / 0
    except ZeroDivisionError:
        errors_logger.exception("Hello this is an error")
