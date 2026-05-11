import logging
from datetime import datetime


def get_logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(f"reports/logs/testlog_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger