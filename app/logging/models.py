"""models

dataclasses for log entries

classes:

    * RequestInfo - class for information about a request
    * LogListEntry - Entries of LogList

Classification: Unclassified
Autor: Lothar Janssen
"""
from dataclasses import dataclass


class RequestInfo:
    """
    class for information about a request
    """
    def __init__(self, request) -> None:
        self.request = request

    @property
    def method(self) -> str:
        """
        method for information about a request
        :return: str of method name
        """
        return str(self.request.method)

    @property
    def route(self) -> str:
        """
        route for information about a request
        :return: str of route name
        """
        return self.request["path"]

    @property
    def ip(self) -> str:
        """
        ip for information about a request
        :return: str of ip
        """
        return str(self.request.client.host)

    @property
    def url(self) -> str:
        """
        url for information about a request
        :return: str of url
        """
        return str(self.request.url)

    @property
    def host(self) -> str:
        """
        host for information about a request
        :return: str of host
        """
        return str(self.request.url.hostname)

    @property
    def headers(self) -> dict or None:
        """
        headers for information about a request
        :return: dict or None
        """
        return {key: value for key, value in self.request.headers.items()}

    @property
    def body(self) -> dict or None:
        """
        body for information about a request
        :return: dict or None
        """
        return self.request.state.body


@dataclass()
class LogListEntry:
    """
    dataclass for log entries
    """
    time: str
    level: str
    massage: str
    file_name: str
    func_name: str
    module: str