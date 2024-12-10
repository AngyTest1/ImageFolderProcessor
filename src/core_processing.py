
from PIL import Image

def process_folder(folder_path):
    try:
        images = [Image.open(os.path.join(folder_path, img)) for img in os.listdir(folder_path) if img.endswith('.jpg')]
        for img in images:
            resize_image(img, (100, 100))
            save_image(img, os.path.join(folder_path, f"resized_{img.filename}"))
    except Exception as e:
        print(f"Error processing folder: {e}")

def resize_image(image, size):
    try:
        resized_img = image.resize(size)
        return resized_img
    except Exception as e:
        print(f"Error resizing image: {e}")

def save_image(image, output_path):
    try:
        image.save(output_path)
    except Exception as e:
        print(f"Error saving image: {e}")