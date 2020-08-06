from common import settings

import logging

logger = logging.getLogger("__main__")

consoleHandle = logging.StreamHandler()

formatter = logging.Formatter(
    ' %(levelname)s: %(asctime)s - %(message)s'
)

consoleHandle.setFormatter(formatter)

logger.addHandler(consoleHandle)

if settings.DEBUG:
    logger.setLevel(logging.DEBUG)


def get_logger():
    return logger
