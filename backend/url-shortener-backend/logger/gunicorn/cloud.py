import logging
import sys

from gunicorn import glogging
from .utils import escape_all_newline_and_quotes
from .constants import LoggerConfig


class CustomFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.msg = escape_all_newline_and_quotes(record.msg)
        record.args = tuple(
            [
                escape_all_newline_and_quotes(arg) if type(arg) == str else arg
                for arg in record.args
            ]
        )
        record.__dict__.setdefault("request_id", "")
        record.__dict__.setdefault("stack_trace", "")
        record.__dict__["stack_trace"] = escape_all_newline_and_quotes(
            record.__dict__["stack_trace"]
        )
        record.__dict__.setdefault("service_name", LoggerConfig.SERVICE_NAME)
        return super().format(record)


class CloudLogger(glogging.Logger):
    ERROR_LOG_FORMAT = {
        "fmt": '{"request_id": "%(request_id)s", "datetime": "%(asctime)s", "services": "%(service_name)s",'
        ' "message": "%(message)s", "stack_trace": "%(stack_trace)s", "loglevel": "%(levelname)s",'
        ' "process_id": "%(process)d"}',
        "datefmt": "%Y-%m-%d %H:%M:%S %z",
    }

    def setup(self, cfg):
        super().setup(cfg)

        formatter = CustomFormatter(**CloudLogger.ERROR_LOG_FORMAT)
        error_logger = logging.getLogger("gunicorn.error")
        warning_logger = logging.getLogger("py.warnings")
        matplotlib_logger = logging.getLogger("matplotlib")
        matplotlib_logger.handlers.clear()

        warning_logger.setLevel(LoggerConfig.LOG_LEVEL.upper())
        matplotlib_logger.setLevel(LoggerConfig.LOG_LEVEL.upper())

        error_logstream = logging.StreamHandler(sys.stdout)
        error_logstream.setFormatter(formatter)
        error_logger.addHandler(error_logstream)
        warning_logger.addHandler(error_logstream)
        matplotlib_logger.addHandler(error_logstream)
