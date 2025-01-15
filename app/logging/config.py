"""config
Here the fallowing functions are defined:

    * define_file_handler - defines file handler
    * define_console_handler - defines console handler
    * define_queue_handler - defines queue handler

Classification: Unclassified
Autor: Lothar Janssen
"""
import logging
import sys

from app.config.service import settings
from app.logging.service import QueueHandler

logger = logging.getLogger("app_logger")

#### File handler ####
def define_file_handler() -> logging.FileHandler:
    """
    method for creating a file handler
    :return: FileHandler filehandler
    """
    if settings.LOG_FILE:
        file_handler = logging.FileHandler(settings.LOG_FILE_PATH)
    else:
        file_handler = logging.NullHandler
    return file_handler


### Console Handler ####
def define_console_handler() -> logging.StreamHandler:
    """
    method for creating a console handler
    :return: StreamHandler console handler
    """
    if settings.LOG_CONSOLE:
        console_handler = logging.StreamHandler(sys.stdout)
    else:
        console_handler = logging.NullHandler
    return console_handler


### Queue Handler
def define_queue_handler() -> QueueHandler:
    """
    method for creating a queue handler
    :return: queue handler
    """

    if settings.LOG_QUEUE:
        queue_handler = QueueHandler()
    else:
        queue_handler = logging.NullHandler
    return queue_handler

# config element
logging.basicConfig(
    level=settings.LOG_LEVEL,
    handlers=[
        QueueHandler(),
        define_file_handler(),
        define_console_handler()
    ]
)
