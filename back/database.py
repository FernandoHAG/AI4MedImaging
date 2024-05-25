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

# Define Image Table
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), nullable=False)
    operations = db.Column(db.String(120), nullable=True)
    processed_image = db.Column(db.LargeBinary, nullable=True)
