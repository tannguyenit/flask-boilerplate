from flask import jsonify, make_response
from typing import Tuple
from flask.wrappers import Response


def success(data: dict = None, status: int = 200, message: str = "") -> Tuple[Response, int]:
    response = {
        "status_code": status,
        "message": message,
        "data": data,
        "error": None
    }

    return make_response(jsonify(response), status)


def error(errors: dict = None, status: int = 400, message: str = "") -> Tuple[Response, int]:
    response = {
        "status_code": status,
        "message": message,
        "data": None,
        "error": errors
    }

    return make_response(jsonify(response), status)
