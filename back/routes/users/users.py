from flask import Blueprint, jsonify

users = Blueprint('users', __name__, static_folder='static')

@users.route('/', methods=['GET'])
def users():
    return jsonify(
        {
            'users': [
                'Fernando',
                'Flor'
            ]
        }
    )