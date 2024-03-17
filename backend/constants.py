from enum import Enum
import os

DOCKER_TAG = os.getenv("DOCKER_TAG", 1)  # pylint: disable=invalid-envvar-default


class ServiceStatus(Enum):
    UP = "up"
    DOWN = "down"
