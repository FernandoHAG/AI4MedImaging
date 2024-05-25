from PIL import Image, ImageEnhance
import os

def process_image(filepath, operation, value):
    image = Image.open(filepath)
    
    if operation == "rotate":
        image = image.rotate(value, expand=True)
    elif operation == "flip":
        if value == 0:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif operation == "contrast":
        enhancer = ImageEnhance.Contrast(image)
        if value <= 0:
            image = enhancer.enhance(0)
        else: 
            image = enhancer.enhance(value)
    elif operation == "brightness":
        enhancer = ImageEnhance.Brightness(image)
        if value <= 0:
            image = enhancer.enhance(0)
        else: 
            image = enhancer.enhance(value)

    return image
