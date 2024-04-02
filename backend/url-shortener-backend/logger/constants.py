from enum import Enum


class LogType(Enum):
    INFO = "info"
    ERROR = "error"
    OUTPUT = "output"


class LoggerName:
    CLOUD = "cloud"


SUPPORTED_LOGGER = [LoggerName.CLOUD]
