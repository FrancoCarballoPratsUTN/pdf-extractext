import logging
import sys

from pythonjsonlogger import json


def setup_logging(log_level: str = "INFO"):
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = json.JsonFormatter(
            fmt="%(asctime)s %(levelname)s %(name)s %(message)s"
        )
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
