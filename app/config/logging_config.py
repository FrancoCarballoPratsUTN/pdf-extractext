import logging
from pythonjsonlogger import jsonlogger
from app.config.settings import settings

loger = logging.getLogger(__name__)
log_level = getattr(logging, settings.log_level, logging.DEBUG)
loger.setLevel(log_level)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

file_handler.setLevel(logging.Warning)

json_formatter = jsonlogger.JsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(json_formatter)
file_handler.setFormatter(json_formatter)

loger.addHandler(console_handler)
loger.addHandler(file_handler)
