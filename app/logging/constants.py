"""constants
Here constants for http exception are defined

    * http_500_unexpected_error

Classification: Unclassified
Autor: Lothar Janssen
"""
def http_500_unexpected_error() -> str:
    return f"Unexpected Error while dispatching request in logging middleware"