from logging import getLogger
from pymongo import MongoClient

logger = getLogger(__name__)
clients = {}


def connect(db, **kwargs):
    if db not in clients:
        logger.debug('New MongoClient connection')
        # Create and reuse a single MongoClient instance
        clients[db] = MongoClient(**kwargs)
    else:
        # Check if the existing MongoClient is closed
        if clients[db]._closed:  # Checking the internal attribute
            logger.debug('MongoClient was closed, creating a new connection')
            clients[db] = MongoClient(**kwargs)
    return clients[db]


class Error(Exception):  # NOQA: StandardError undefined on PY3
    pass


class InterfaceError(Error):
    pass


class DatabaseError(Error):
    pass


class DataError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class InternalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


def Binary(value):
    return value
