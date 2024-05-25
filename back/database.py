from flask_sqlalchemy import SQLAlchemy

# Define Data Bank
db = SQLAlchemy()

# Create Data Bank
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image_processing.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        #db.drop_all()
        db.create_all()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    originalImage = db.Column(db.String(80), nullable=False)
    processedImage = db.Column(db.String(80), nullable=False)

class ImageOperation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idImage = db.Column(db.Integer, nullable=False)
    operation = db.Column(db.String(80), nullable=False)
    operationValue = db.Column(db.String(80), nullable=False)
