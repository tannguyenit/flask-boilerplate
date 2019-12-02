from flask_restplus import Api
from flask import Blueprint, current_app
from werkzeug.local import LocalProxy
from werkzeug.exceptions import BadRequest

from .users.routes import route as user_route
from .auth.routes import route as auth_route

api = Blueprint('api', __name__)
logger = LocalProxy(lambda: current_app.logger)

app = Api(api,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='flask restplus web service'
          )


@app.errorhandler(BadRequest)
def handler_bad_request():
    logger.info('API ERROR')


app.add_namespace(user_route, path='/user')
app.add_namespace(auth_route, path='/auth')
