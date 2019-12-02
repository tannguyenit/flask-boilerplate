"""Application error handlers."""
from flask import Blueprint
from werkzeug.exceptions import HTTPException, BadRequest

from infrastructor.response import error

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(HTTPException)
def handle_unexpected_error(e: HTTPException):
    if isinstance(e, BadRequest):
        if hasattr(e, 'data'):
            return error(e.data.get('errors'), e.code, e.data.get('message'))

        return error(None, e.code, e.description)
