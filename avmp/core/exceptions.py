"""User-defined exceptions.
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"


class Error(Exception):
    """Base class for other exceptions"""
    pass


class APIConnectionError(Error):
    """Raided when connection to API breaks"""
    pass


class MissingConfiguration(Error):
    """Missing variables in configuration file"""
    pass