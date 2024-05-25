from flask import Blueprint, request, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename
from database import db, Image, ImageOperation
import os
from utils.image_processing import process_image
import datetime
import shutil
import math

router = Blueprint('router', __name__, static_folder='static')

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tiff'}

def allowedFile(filename):
    return filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

def getImageName(filename):
    now = datetime.datetime.now()
    milliseconds = math.floor((now.timestamp() * 1000) + (now.microsecond / 1000))
    return str(milliseconds) + "." +filename.rsplit('.', 1)[-1].lower()

@router.route('/', methods=['GET'])
def test():
    return 'OK'

@router.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "no file key!"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file addrs"}), 400

    if file and allowedFile(file.filename):
        filename = getImageName(file.filename)
        originalFilepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(originalFilepath)
        processedFilepath = os.path.join(PROCESSED_FOLDER, filename)
        shutil.copy(originalFilepath, processedFilepath)

        new_image = Image(originalImage=filename, processedImage=filename)
        db.session.add(new_image)
        db.session.commit()

        images = Image.query.all()
        images_list = [{"id": image.id, "image": image.processedImage} for image in images]
        return jsonify(images_list), 201

    return jsonify({"error": "File type not allowed"}), 400

@router.route('/images', methods=['GET'])
def list_images():
    images = Image.query.all()
    images_list = [{"id": image.id, "image": image.processedImage} for image in images]
    return jsonify(images_list), 200

@router.route('/imageFile', methods=['GET'])
def get_image():
    if 'id' not in request.args:
        return jsonify({"error": "no id key!"}), 400
    id = request.args.get('id')

    image = Image.query.get(id)
    if image is None:
        return jsonify({"error": "Image not found"}), 404

    return send_from_directory(PROCESSED_FOLDER, image.processedImage, mimetype='image/png')

@router.route('/process', methods=['PUT'])
def process_uploaded_image():
    if 'id' not in request.args:
        return jsonify({"error": "no id key!"}), 400
    if 'operation' not in request.args:
        return jsonify({"error": "no operation key!"}), 400
    if 'value' not in request.args:
        return jsonify({"error": "no value key!"}), 400

    
    id = request.args.get('id')
    operation = request.args.get('operation')
    value = request.args.get('value')

    image = Image.query.get(id)
    if not image:
        return jsonify({"error": "Image not found"}), 404

    filepath = os.path.join(PROCESSED_FOLDER, image.processedImage)
    processedImage = process_image(filepath, operation, value)
    processedImage.save(filepath)
    newOperation = ImageOperation(idImage=image.id, operation=operation, operationValue=value)
    db.session.add(newOperation)
    db.session.commit()

    return send_from_directory(PROCESSED_FOLDER, image.processedImage, mimetype='image/png')