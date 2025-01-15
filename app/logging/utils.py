"""utils

Class to filter sensitive information like ip and password

classes:

    * SensitiveDataFilter - class for filtering sensitive data in a LogRecord object

Classification: Unclassified
Autor: Lothar Janssen
"""
import logging
import re

class SensitiveDataFilter(logging.Filter):
    # list of keys that values are sensitive data
    SENSITIVE_KEYS = (
        "credentials",
        "authorization",
        "token",
        "password",
        "access_token",
    )
    TOKEN_PATTERN = rf"token=([^;]+)"

    def filter(self, record) -> bool:
        """
        method to filter sensitive data
        :param record: log record which to filter
        :return: bool resulting from filtering
        """
        try:
            record.args = self.mask_sensitive_args(record.args)
            record.msg = self.mask_sensitive_msg(record.msg)
            return True
        except Exception as e:
            # not useful to generate log outside filter, so always return true
            return True

    def mask_sensitive_args(self, args):
        """
        method to mask sensitive data
        :param args: elements to filter sensitive data
        :return: masked sensitive attributes
        """
        if isinstance(args, dict):
            new_args = args.copy()
            for key in args.keys():
                if key.lower() in self.SENSITIVE_KEYS:
                    new_args[key] = "******"
                else:
                    # mask sensitive data in dict values
                    new_args[key] = self.mask_sensitive_msg(args[key])
            return new_args
        # when there are multi arg in record.args
        return tuple([self.mask_sensitive_msg(arg) for arg in args])

    def mask_sensitive_msg(self, message):
        """
        method to mask sensitive data
        :param message: message to mask
        :return: clean sensitive message
        """
        # mask sensitive data in multi record.args
        if isinstance(message, dict):
            return self.mask_sensitive_args(message)
        if isinstance(message, str):
            replace = f"token=******"
            message = re.sub(self.TOKEN_PATTERN, replace, message)
        return message