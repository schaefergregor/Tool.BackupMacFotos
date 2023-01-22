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

def copy_images(folderPath):
    images = os.listdir(folderPath)
    for image in images:
        imageSourcePath = os.path.join(folderPath, image)
        if os.path.isdir(imageSourcePath):
            print("File is a folder => Skip")
            continue

        if image == ".DS_Store":
            print("File is .DS_Store => Skip")
            continue

        target_folder = get_target_folder_path(imageSourcePath)
        if not os.path.isdir(target_folder):
            os.makedirs(target_folder, exist_ok=True)

        targetImagePath = os.path.join(target_folder, image)

        print(f'Begin copy file {imageSourcePath} to {target_folder}')
        shutil.copyfile(imageSourcePath, targetImagePath)

def initialize():
    image_folders = os.listdir(config_parser.input_dir)
    for folder in image_folders:
        folderPath = os.path.join(config_parser.input_dir, folder)
        if not os.path.isdir(folderPath):
            continue

        copy_images(folderPath)