"""
Module for image copy.
"""
import os
import time
import shutil
import argument_parser


def get_target_folder_path(image_path):
    """
    Gets the new folder name.
    """
    last_modification_time = os.path.getmtime(image_path)
    last_modification_time_in_seconds = time.ctime(last_modification_time)
    last_modification_time_timestamp = time.strptime(last_modification_time_in_seconds)
    last_modification_time_year = time.strftime("%Y", last_modification_time_timestamp)
    last_modification_time_month = time.strftime("%m", last_modification_time_timestamp)
    
    return os.path.join(argument_parser.OUTPUT_DIR, last_modification_time_year, last_modification_time_month)


def copy_images(image):
    """
    Copies image to the given output dir.
    """
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

    target_image_path = os.path.join(target_folder, image_filename)
    shutil.copyfile(image, target_image_path)


def collect_images():
    """
    Collects all images in the given input dir.
    """
    images = []
    for dirpath, _, filenames in os.walk(argument_parser.INPUT_DIR):
        for filename in filenames:
            images.append(os.path.join(dirpath, filename))
    return images


def initialize():
    """
    Initializes the image copy.
    """
    images = collect_images()

    print(f'Begin copy amount of {len(images)} to target folder.')
    for index, image in enumerate(images):
        print(f'Copy image {str(index+1)} / {str(len(images))}.')
        copy_images(image)
