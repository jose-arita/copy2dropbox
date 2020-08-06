import logging

logger = logging.getLogger("__main__")

consoleHandle = logging.StreamHandler()

formatter = logging.Formatter(
    ' %(levelname)s: %(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

consoleHandle.setFormatter(formatter)

logger.addHandler(consoleHandle)


def get_logger():
    return logger
