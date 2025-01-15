"""events

These events are calling

functions:

    * execute_backend_server_event_handler - event for initializing db connection
    * terminate_backend_server_event_handler - event for disposing db connection

Classification: Unclassified
Autor: Lothar Janssen
"""
import typing

from app.db.events import dispose_db_connection, initialize_db_connection


def execute_backend_server_event_handler() -> typing.Any:
    """
    This static function is initialized to execute the backend server event handler
    :return: typing anything
    """
    async def launch_backend_server_events() -> None:
        await initialize_db_connection()

    return launch_backend_server_events


def terminate_backend_server_event_handler() -> typing.Any:
    """
    This static function is initialized to terminate the backend server event handler
    :return: typing anything
    """
    async def stop_backend_server_events() -> None:
        await dispose_db_connection()

    return stop_backend_server_events