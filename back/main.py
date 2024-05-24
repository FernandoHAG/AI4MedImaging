from flask import Flask
from flask_cors import CORS
from routes.router import router

app = Flask(__name__)
cors = CORS(app, origins='*')
app.register_blueprint(router, url_prefix='')

if __name__ == '__main__':
    app.run(debug=True, port=8080)