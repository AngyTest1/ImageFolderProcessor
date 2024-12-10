import os
from PIL import Image

def get_folders_in_directory(directory):
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

def copy_and_rename_images(original_image_path, parent_folder, org_folder, version_name):
    new_image_file = f"{version_name}_{os.path.basename(original_image_path)}"
    new_image_path = os.path.join(org_folder, new_image_file)
    
    # Copy and rename image
    with open(original_image_path, "rb") as original:
        with open(new_image_path, "wb") as new:
            new.write(original.read())

def scale_image(image_path, output_path, width, height):
    img = Image.open(image_path)
    resized_img = img.resize((width, height))
    resized_img.save(output_path)