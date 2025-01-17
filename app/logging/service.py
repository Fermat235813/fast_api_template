"""logging

Main class of application

classes:

    * SensitiveDataFilter - class for filtering sensitive data in a LogRecord object

Classification: Unclassified
Autor: Lothar Janssen
"""
import logging
from functools import lru_cache
from asyncio.queues import Queue
from logging import LogRecord

from app.config.service import settings
from app.logging.models import LogListEntry



class LoggingQueue:
    """
    class which defines logging queue
    """
    def __init__(self, max_size: int):
        self.queue: Queue = Queue(maxsize=max_size)

    def add_element(self, element):
        """
        method to add element to queue
        :param element: element to add
        :return: current queue
        """
        return self.queue.put_nowait(element)

    def get_values(self):
        """
        method to get values from queue
        :return: all LogRecord objects
        """
        return self.queue

    def get_current_element(self):
        """
        method to get current element
        :return: current LogListEntry object
        """
        return self.queue.get_nowait()


@lru_cache(maxsize=1)
def get_queue() -> LoggingQueue:
    """
    Method to get queue
    :return: LoggingQueue
    """
    return LoggingQueue(settings.LOG_QUEUE_MAX_SIZE)

logging_queue: LoggingQueue = get_queue()


class QueueHandler(logging.Handler):
    """
    A handler class which allows the cursor to stay on
    one line for selected messages
    """

    def emit(self, record: LogRecord) -> None:
        """
        :param record: record to process
        :return: nothing
        """
        entry = LogListEntry("",record.levelname, record.msg,
                   record.filename, record.funcName,record.module)
        logging_queue.add_element(entry)