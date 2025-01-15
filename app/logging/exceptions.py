"""exception
Here exception to package logging are handled

This file contains the following
function:

    * http_exc_500_unexpected_error - handles HTTP 500 unexpected error

Classification: Unclassified
Autor: Lothar Janssen
"""
import fastapi
from app.logging.constants import http_500_unexpected_error

async def http_exc_500_unexpected_error() -> Exception:
    """
    method to handle http 500 unexpected error
    :return: Exception raised if credentials are invalid
    """
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_400_BAD_REQUEST,
        detail= http_500_unexpected_error()
    )