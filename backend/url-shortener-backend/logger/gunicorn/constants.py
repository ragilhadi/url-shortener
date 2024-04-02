class LoggerName:
    CLOUD = "cloud"


class LoggerConfig:
    LOG_LEVEL = ""
    SERVICE_NAME = ""


class AccessLogConfig:
    OUTPUT = "output"
    FORMAT = "format"


def set_log_level(log_level: str):
    LoggerConfig.LOG_LEVEL = log_level


def set_service_name(service_name: str):
    LoggerConfig.SERVICE_NAME = service_name
