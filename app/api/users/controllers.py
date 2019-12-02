from flask import request
from flask_restplus import Resource

from infrastructor.utils import validate
from infrastructor.response import success
from app.api.users.request import Request
from ..users import route

index_rule = Request.index_request()
store_request = Request.store_request()


class UserIndex(Resource):
    @staticmethod
    @route.response(200, 'OK')
    @route.response(400, 'Bad Request')
    @route.expect(index_rule, validate=True)
    def get():
        data = validate(index_rule)

        return success(data)

    @route.response(200, 'OK')
    @route.response(400, 'Bad Request')
    @route.expect(store_request)
    def put(self):
        data = request.json

        return success(data)


class UserDetail(Resource):
    @staticmethod
    def get(user_id: int):
        return success({'user_id': user_id})
