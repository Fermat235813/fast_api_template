"""Logging router
Here the main entry points of logging are added.

This file contains the following
functions:

    * get_logging_queue - return the hole queue
    * get_next_entry - returns the next entry of queue
    and deletes after returning

Classification: Unclassified
Autor: Lothar Janssen
"""
from asyncio import Queue

from fastapi import APIRouter
from app.logging.service import logging_queue

log_router = APIRouter()


@log_router.get("/logging/get_all")
async def get_logging_queue():
    """
    Returns the logs queue
    """
    log = logging_queue.get_values()
    return log


@log_router.get("/logging/get_next_entry")
async def get_next_entry():
    """
    Deleting and returning the next log entry
    """

    retval =  logging_queue.get_current_element()
    return retval