from .controllers import *
from . import route

route.add_resource(AuthLogin, '/login')
