import logging
from pythonjsonlogger import json
from app.config.settings import settings

loger = logging.getLogger("pdf-extractext")
log_level = getattr(logging, settings.log_level, logging.DEBUG)
loger.setLevel(log_level)

console_handler = logging.StreamHandler()

json_formatter = json.JsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(json_formatter)

loger.addHandler(console_handler)
