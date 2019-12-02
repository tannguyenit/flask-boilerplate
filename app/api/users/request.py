from flask_restplus import fields
from ..users import route


class Request:
    @staticmethod
    def index_request():
        rules = route.parser()
        rules.add_argument('search', type=str)

        return rules

    @staticmethod
    def store_request():
        return route.model('users', {
            'email': fields.String(required=True, description='user email address'),
            'username': fields.Integer(required=True, description='user username'),
            'password': fields.String(required=True, description='user password')
        })
