from enum import Enum


class StatusCodes(Enum):
    """List of common HTTP status codes"""
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101
    PROCESSING = 102
    REQUEST_URI_TOO_LONG = 122
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    MULTIPLE_CHOICES = 300
    MOVED = 301
    FOUND = 302
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
