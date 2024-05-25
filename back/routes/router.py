from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from database import db, Image
import os
from utils.image_processing import process_image

router = Blueprint('router', __name__, static_folder='static')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@router.route('/', methods=['GET'])
def test():
    return 'OK'

@router.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        new_image = Image(filename=filename)
        db.session.add(new_image)
        db.session.commit()

        return jsonify({"message": "File successfully uploaded"}), 201

    return jsonify({"error": "File type not allowed"}), 400

@router.route('/images', methods=['GET'])
def list_images():
    images = Image.query.all()
    images_list = [{"id": image.id, "filename": image.filename} for image in images]
    return jsonify(images_list), 200

@router.route('/process', methods=['POST'])
def process_uploaded_image():
    data = request.get_json()
    image_id = data.get('image_id')
    operation = data.get('operation')

    image = Image.query.get(image_id)
    if not image:
        return jsonify({"error": "Image not found"}), 404

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    processed_filepath = process_image(filepath, operation)

    with open(processed_filepath, "rb") as f:
        processed_image_data = f.read()

    image.operations = operation
    image.processed_image = processed_image_data
    db.session.commit()

    return jsonify({"message": "Image processed successfully"}), 200