from flask_restplus import fields
from ..auth import route

login_request = route.model('auth_login', {
    'email': fields.String(required=True, description='The email address'),
    'password': fields.String(required=True, description='The user password '),
})
