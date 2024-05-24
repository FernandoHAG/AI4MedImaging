from flask import Blueprint

router = Blueprint('router', __name__, static_folder='static')

@router.route('/', methods=['GET'])
def test():
    return 'OK'