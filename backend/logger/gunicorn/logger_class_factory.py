from ..constants import LoggerName
from .cloud import CloudLogger

from typing import Type
from gunicorn import glogging


class LoggerClassFactory:
    @staticmethod
    def get_logger_class(logger_name: str) -> Type[glogging.Logger]:
        if logger_name == LoggerName.CLOUD:
            return CloudLogger
        else:
            raise ValueError(f"LOGGER_NAME: {logger_name} does not exists.")
