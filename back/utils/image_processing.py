from PIL import Image, ImageEnhance
import os

def process_image(filepath, operation):
    image = Image.open(filepath)
    
    if operation == "rotate_90":
        image = image.rotate(90, expand=True)
    elif operation == "rotate_180":
        image = image.rotate(180, expand=True)
    elif operation == "flip_horizontal":
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif operation == "flip_vertical":
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif operation == "increase_contrast":
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)
    elif operation == "decrease_contrast":
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(0.5)
    elif operation == "increase_brightness":
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(2)
    elif operation == "decrease_brightness":
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(0.5)

    processed_filepath = f"{os.path.splitext(filepath)[0]}_{operation}.png"
    image.save(processed_filepath)
    return processed_filepath
