from typing import Callable

from .constants import LoggerName


class LoggerRegistry:
    _REGISTRY = dict()
    _DEFAULT = LoggerName.CLOUD

    @classmethod
    def get(cls, logger_name: str) -> Callable:
        if logger_name in cls._REGISTRY:
            return cls._REGISTRY[logger_name]
        return cls._REGISTRY[cls._DEFAULT]

    @classmethod
    def register_logger(cls, logger_name: str) -> Callable:
        def _inner(logger_class):
            nonlocal logger_name
            cls._REGISTRY[logger_name] = logger_class
            return logger_class

        return _inner
