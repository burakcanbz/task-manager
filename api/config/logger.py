import logging
import asyncio
from threading import Lock
from typing import Optional

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"


class AsyncLogger:
    _instance: Optional["AsyncLogger"] = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._initialized = True

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.logger.handlers.clear()

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        self.logger.addHandler(console_handler)

        # File handler
        file_handler = logging.FileHandler("app.log", encoding="utf-8", delay=True)
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        self.logger.addHandler(file_handler)

    # Override methods to run every process in different thread to prevent blocking operation.
    async def info(self, message: str):
        await asyncio.to_thread(self.logger.info, message)

    async def error(self, message: str):
        await asyncio.to_thread(self.logger.error, message)

    async def warning(self, message: str):
        await asyncio.to_thread(self.logger.warning, message)

    async def debug(self, message: str):
        await asyncio.to_thread(self.logger.debug, message)

    async def critical(self, message: str):
        await asyncio.to_thread(self.logger.critical, message)

    def get_logger(self):
        return self.logger


# Global instance
_logger_instance = AsyncLogger()
logger = _logger_instance
