"""logging

Schema for LogEntries

classes:

    * RequestLog - class for defining Request Log
    * ResponseLog - class for defining Response Log

Classification: Unclassified
Autor: Lothar Janssen
"""
from pydantic import BaseModel

class RequestLog(BaseModel):
    """
    class defines Request Log
    """
    req_id: str
    method: str
    route: str
    ip: str
    url: str
    host: str
    body: dict = None
    headers: dict = None

class ErrorLog(BaseModel):
    """
    class defines Error Log
    """
    req_id: str
    error_message: str