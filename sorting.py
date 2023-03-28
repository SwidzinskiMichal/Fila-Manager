from distutils.command.config import config
import os
import json
import shutil
import json
from pathlib import Path

with open("config.json") as config_dict:
    config = json.load(config_dict)
    file_categories = config["file_categories"]

def sort_files(path):
    for name in os.listdir(path):
        for file_category in file_categories:
            if Path(name).suffix in file_category["file_extensions"]:
                category_name = file_category["name"]
                shutil.move(f"{path}/{name}", f"{path}/{category_name}")
                    
def remove_empty_directories(path):
    for name in os.listdir(path):
        if is_dir_empty(f"{path}/{name}"):
            os.rmdir(f"{path}/{name}")

def remove_created_empty_directories(path):
    created_folders = [category["name"] for category in file_categories]
    for name in os.listdir(path):
        if is_dir_empty(f"{path}/{name}") and name in created_folders:
            os.rmdir(f"{path}/{name}")

def setup_directories(path):
    expected_directories = [category["name"] for category in file_categories]
    for directory in expected_directories:
        if not os.path.exists(f"{path}/{directory}"):
            os.makedirs(f"{path}/{directory}")


with open('config_dicts.txt') as f:
    config_dicts = f.read()
expected_directories = config_dicts.split(",")

with open('config_extensions.txt') as f:
    config_extensions = f.read()
file_categories = json.loads(config_extensions)


def sort_files(chosen_directory):
    for file in os.listdir(chosen_directory):
        for category, extensions in file_categories.items():
            if Path(file).suffix in extensions:
                shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/{category}")


def clean_empty_directories(chosen_directory):
    for directory in os.listdir(chosen_directory):
        if len(os.listdir(f"{chosen_directory}/{directory}")) == 0:
            os.rmdir(f"{chosen_directory}/{directory}")
        else:
            pass
            
def is_dir_empty(path_to_check):
    if not os.path.isdir(path_to_check):
        return False

    if len(os.listdir(path_to_check)) == 0:
        return True

    return False


def setup_directories(path):
    expected_directories = [category["name"] for category in file_categories]
    for directory in expected_directories:
        if not os.path.exists(f"{path}/{directory}"):
            os.makedirs(f"{path}/{directory}")

