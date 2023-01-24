import os
import time
import shutil
import config_parser

def get_target_folder_path(imageSourcePath):
    modifiedTime = os.path.getmtime(imageSourcePath)
    modifiedTimeAsTime = time.ctime(modifiedTime)
    modifiedTimestamp = time.strptime(modifiedTimeAsTime)
    modifiedYear = time.strftime("%Y", modifiedTimestamp)
    modifiedMonth = time.strftime("%m", modifiedTimestamp)
    
    return os.path.join(config_parser.output_dir, modifiedYear, modifiedMonth)

def copy_images(image):
    if os.path.isdir(image):
        print("File is a folder => Skip")
        return

    if image == ".DS_Store":
        print("File is .DS_Store => Skip")
        return

    image_filename = os.path.basename(image)
    target_folder = get_target_folder_path(image)
    if not os.path.isdir(target_folder):
        os.makedirs(target_folder, exist_ok=True)

    targetImagePath = os.path.join(target_folder, image_filename)
    shutil.copyfile(image, targetImagePath)

def collect_images():
    images = []
    for dirpath, _, filenames in os.walk(config_parser.input_dir):
        for filename in filenames:
            images.append(os.path.join(dirpath, filename))
    return images

def initialize():
    images = collect_images()

    print(f'Begin copy amount of {len(images)} to target folder.')
    for index, image in enumerate(images):
        print(f'Copy image {str(index+1)} / {str(len(images))}.')
        copy_images(image)
