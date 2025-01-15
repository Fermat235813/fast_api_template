"""dependencies
Here the main entry points of logging are added.

This file contains the following
functions / classes:

    * log_request - define record in a request and log it
    * log_error - define record in a request and log it
    * log_middleware - middleware for dispatching request

Classification: Unclassified
Autor: Lothar Janssen
"""
import traceback
import uuid
import json

from fastapi import Request, Response
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware

from app.logging.exceptions import http_exc_500_unexpected_error
from app.logging.schemas import RequestLog, ErrorLog
from app.logging.models import RequestInfo
from app.logging.service import get_logger


def log_request(request: Request) -> None:
    """
    static method for logging requests
    :param request: Request object to log
    :return: nothing
    """
    request_info = RequestInfo(request)
    request_log = RequestLog(
        req_id=request.state.req_id,
        method=request_info.method,
        route=request_info.route,
        ip=request_info.ip,
        url=request_info.url,
        host=request_info.host,
        body=request_info.body,
        headers=request_info.headers,
    )
    get_logger().info(request_log.dict())


def log_error(uuid: str, response_body: dict) -> None:
    """
    static method for logging errors
    :param uuid: id of the error
    :param response_body: response body defined in a dict
    :return: nothing
    """
    error_log = ErrorLog(
        req_id=uuid,
        error_message=response_body["error_message"],
    )
    get_logger().error(error_log.dict())
    get_logger().error(traceback.format_exc())


class LogMiddleware(BaseHTTPMiddleware):
    """
    Represents middleware for logging requests
    """
    def __init__(self,app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        """
        :param request: Request object to log
        :param call_next: call of next request
        :return: Response object
        """
        req_id = str(uuid.uuid4())

        try:
            #### request ####
            request.state.req_id = req_id
            request.state.body = json.loads(await request.body() or "{}")
            log_request(request)

            #### response ####
            response = await call_next(request)
            response_body = ""
            if response.headers.get("content-type") == "application/json":
                response_body = [chunk async for chunk in response.body_iterator]
                response.body_iterator = iterate_in_threadpool(iter(response_body))
            return response

        except Exception as e:
            # Unexpected error handling
            log_error(req_id, {"error_message": "ERR_UNEXPECTED"})
            raise http_exc_500_unexpected_error()