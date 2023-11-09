import logging
import os
import sys

import rollbar
from settings import config, Environment
from rollbar.logger import RollbarHandler

ROLLBAR_ACCESS_TOKEN = config.ROLLBAR_ACCESS_TOKEN
ROLLBAR_ENVIRONMENT = config.APP_ENV.value

if ROLLBAR_ACCESS_TOKEN:
    rollbar.init(
        access_token=config.ROLLBAR_ACCESS_TOKEN,
        environment=config.APP_ENV.value,
        root=os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        allow_logging_basic_config=False
    )


def _get_log_level():
    if config.APP_ENV != Environment.development:
        return logging.DEBUG
    loglevel = getattr(config, 'LOGLEVEL', 'INFO')
    return getattr(logging, loglevel, 'INFO')


def _get_formatter():
    return logging.Formatter('%(asctime)s [%(levelname)s] %(module)s:%(lineno)d - %(message)s')


def rollbar_except_hook(exc_type, exc_value, traceback):
    # Report the issue to rollbar here.
    rollbar.report_exc_info((exc_type, exc_value, traceback))
    # display the error as normal here
    sys.__excepthook__(exc_type, exc_value, traceback)


def set_rollbar_exception_catch():
    sys.excepthook = rollbar_except_hook


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(_get_formatter())
    return console_handler


def get_rollbar_handler():
    rollbar_handler = RollbarHandler(access_token=ROLLBAR_ACCESS_TOKEN, environment=ROLLBAR_ENVIRONMENT)
    rollbar_handler.setLevel(logging.WARNING)
    return rollbar_handler


def create_logger(logger_name=__name__):
    logger = logging.getLogger(logger_name)

    logger.handlers.clear()

    logger.setLevel(_get_log_level())

    logger.addHandler(get_console_handler())

    if ROLLBAR_ACCESS_TOKEN:
        logger.addHandler(get_rollbar_handler())

    logger.propagate = False
    return logger


def get_logger(logger_name):
    return logging.getLogger(logger_name)


logger = get_logger(__name__)
