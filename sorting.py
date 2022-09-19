import os
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
        if os.path.isdir(f"{path}/{name}") and len(os.listdir(f"{path}/{name}")) == 0:
            os.rmdir(f"{path}/{name}")

def remove_created_empty_directories(path):
    created_folders = [category["name"] for category in file_categories]
    for name in os.listdir(path):
        if os.path.isdir(f"{path}/{name}") and len(os.listdir(f"{path}/{name}")) == 0 and name in created_folders:
            os.rmdir(f"{path}/{name}")

def setup_directories(path):
    expected_directories = [category["name"] for category in file_categories]
    for directory in expected_directories:
        if not os.path.exists(f"{path}/{directory}"):
            os.makedirs(f"{path}/{directory}")

def is_dir_empty(path, name):
    if not os.path.isdir(f"{path}/{name}"):
        raise Exception("Directory not found.")

    if len(os.listdir(f"{path}/{name}")) == 0:
        return True

    return False
