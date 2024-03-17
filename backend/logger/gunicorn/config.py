from .constants import AccessLogConfig, LoggerName


def get_accesslog_config(logger_name: str):
    ACCESS_LOG_CONFIG = {  # pylint: disable=invalid-name
        LoggerName.CLOUD: {AccessLogConfig.OUTPUT: None, AccessLogConfig.FORMAT: ""},
    }

    if logger_name not in ACCESS_LOG_CONFIG:
        raise ValueError(f"LOGGER_NAME: {logger_name} does not exists.")

    return ACCESS_LOG_CONFIG[logger_name]
