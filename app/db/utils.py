"""utils

Here general utils for main application is defined

functions:

    * format_datetime_into_iso_format - date formatter
    * format_dict_key_to_camel_case - splitting camelcase

Classification: Unclassified
Autor: Lothar Janssen
"""
import datetime


def format_datetime_into_iso_format(date_time: datetime.datetime) -> str:
    """
    this function formats a datetime object to ISO format
    :param date_time: time with format '%Y-%m-%dT%H:%M:%S'
    :return: date_time in iso format
    """
    return date_time.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")

def format_dict_key_to_camel_case(dict_key: str) -> str:
    """
    this function formats a dictionary key to camelCase
    :param dict_key: dictionary key to camelcase
    :return: datetime
    """
    return "".join(word if idx == 0 else word.capitalize() for idx, word in enumerate(dict_key.split("_")))