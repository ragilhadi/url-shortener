from typing import Union

from flask import Flask

from .logger_registry import LoggerRegistry
from .constants import LoggerName, LogType


@LoggerRegistry.register_logger(logger_name=LoggerName.CLOUD)
class CloudLogger:
    def __init__(self, app: Flask, service_name: str):
        self.app = app
        self.service_name = service_name

    def __call__(
        self,
        request_method: str,
        response: Union[str, dict],
        message: str,
        stack_trace: str,
        log_type: LogType,
    ):
        if log_type == LogType.ERROR:
            self.app.logger.error(
                message,
                extra={
                    "request_id": self.app.request_id,
                    "service_name": self.service_name,
                    "stack_trace": stack_trace,
                },
            )
        else:
            self.app.logger.info(
                message,
                extra={
                    "request_id": self.app.request_id,
                    "service_name": self.service_name,
                    "stack_trace": stack_trace,
                },
            )
