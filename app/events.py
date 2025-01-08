import typing


from app.db.events import dispose_db_connection, initialize_db_connection


def execute_backend_server_event_handler() -> typing.Any:
    async def launch_backend_server_events() -> None:
        await initialize_db_connection()

    return launch_backend_server_events


def terminate_backend_server_event_handler() -> typing.Any:
    async def stop_backend_server_events() -> None:
        await dispose_db_connection()

    return stop_backend_server_events