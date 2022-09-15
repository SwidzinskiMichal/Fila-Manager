import os
import shutil
import json
from pathlib import Path


with open("config.json") as config_dict:
    config = json.load(config_dict)
    file_categories = config["file_categories"]


def sort_files(chosen_directory):
    for name in os.listdir(chosen_directory):
        for file_category in file_categories:
            if Path(name).suffix in file_category["file_extensions"]:
                category_name = file_category["name"]
                shutil.move(f"{chosen_directory}/{name}", f"{chosen_directory}/{category_name}")


def remove_empty_directories(chosen_directory):
    for name in os.listdir(chosen_directory):
        if os.path.isdir(f"{chosen_directory}/{name}") and len(os.listdir(f"{chosen_directory}/{name}")) == 0:
            os.rmdir(f"{chosen_directory}/{name}")

def remove_created_empty_directories(chosen_directory):
    file_categories_string = f"{file_categories}"
    for name in os.listdir(chosen_directory):
        if os.path.isdir(f"{chosen_directory}/{name}") and len(os.listdir(f"{chosen_directory}/{name}")) == 0 and name in file_categories_string:
            os.rmdir(f"{chosen_directory}/{name}")

def setup_directories(chosen_directory):
    expected_directories = list(file_categories.keys())
    for directory in expected_directories:
        if not os.path.exists(f"{chosen_directory}/{directory}"):
            os.makedirs(f"{chosen_directory}/{directory}")
