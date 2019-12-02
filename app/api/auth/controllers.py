from flask import request
from flask_restplus import Resource

from app.api.auth.request import login_request
from ..auth import route
from .services import AuthService


@route.route('/login')
class AuthLogin(Resource):
    """
        User Login Resource
    """
    @route.doc('user login')
    @route.expect(login_request, validate=True)
    def post(self):
        post_data = request.json
        return AuthService.login_user(data=post_data)


@route.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @route.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return AuthService.logout_user(data=auth_header)
