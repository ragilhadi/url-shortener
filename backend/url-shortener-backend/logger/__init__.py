import os
from flask import Flask

from .logger_registry import LoggerRegistry
from . import cloud
from .constants import LoggerName, SUPPORTED_LOGGER, LogType


LOGGER_NAME = os.environ.get("LOGGER_NAME", LoggerName.CLOUD)
if LOGGER_NAME not in SUPPORTED_LOGGER:
    raise ValueError(f"LOGGER_NAME: {LOGGER_NAME} does not exist.")

LOGGER_CLASS = LoggerRegistry.get(LOGGER_NAME)
LOGGER = None


def instantiate_logger(app: Flask, service_name: str):
    global LOGGER  # pylint: disable=global-statement
    LOGGER = LOGGER_CLASS(app, service_name)


def get_logger():
    global LOGGER  # pylint: disable=global-variable-not-assigned
    return LOGGER
