import os
from logger.gunicorn import (
    AccessLogConfig,
    LoggerClassFactory,
    set_log_level,
    set_service_name,
    get_accesslog_config,
)

workers = os.getenv("GUNICORN_WORKERS", 1)  # pylint: disable=invalid-envvar-default
bind = os.getenv(f"0.0.0.0:{os.getenv('BIND_PORT')}", "0.0.0.0:8810")
max_requests = int(
    os.getenv("GUNICORN_MAX_REQUESTS", 15)  # pylint: disable=invalid-envvar-default
)
max_requests_jitter = int(
    os.getenv(  # pylint: disable=invalid-envvar-default
        "GUNICORN_MAX_REQUESTS_JITTER", 5
    )
)
timeout = int(
    os.getenv("GUNICORN_TIMEOUT", 120)  # pylint: disable=invalid-envvar-default
)
reload = True

loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")
logger_name = os.getenv("GUNICORN_LOGGER_NAME", "cloud")

set_log_level(loglevel)
set_service_name(os.getenv("SERVICE_NAME", "flask_api"))

accesslog_config = get_accesslog_config(logger_name)
accesslog = accesslog_config[AccessLogConfig.OUTPUT]
access_log_format = accesslog_config[AccessLogConfig.FORMAT]
errorlog = None
logger_class = LoggerClassFactory.get_logger_class(logger_name)
