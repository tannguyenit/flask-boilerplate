from .controllers import *
from ..users import route

route.add_resource(UserIndex, '/')
route.add_resource(UserDetail, '/<user_id>')
