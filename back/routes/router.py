from flask import Blueprint, jsonify
from users.users import users

router = Blueprint('router', __name__, static_folder='static')
router.register_blueprint(router, url_prefix='/users')

@router.route('/', methods=['GET'])
def test():
    return 'OK'