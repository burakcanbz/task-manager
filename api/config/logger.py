import logging

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False 

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(LOG_FORMAT)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler("app.log", encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(LOG_FORMAT)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)