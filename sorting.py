import os
import shutil
import json
from pathlib import Path


with open("config.json") as config_dict:
    file_categories = json.load(config_dict)


def sort_files(chosen_directory):
    for name in os.listdir(chosen_directory):
        for category, extensions in file_categories.items():
            if Path(name).suffix in extensions:
                shutil.move(f"{chosen_directory}/{name}", f"{chosen_directory}/{category}")


def remove_empty_directories(chosen_directory):
    for name in os.listdir(chosen_directory):
        if os.path.isdir(f"{chosen_directory}/{name}") and len(os.listdir(f"{chosen_directory}/{name}")) == 0:
            os.rmdir(f"{chosen_directory}/{name}")


def setup_directories(chosen_directory):
    expected_directories = list(file_categories.keys())    
    for directory in expected_directories:
        if not os.path.exists(f"{chosen_directory}/{directory}"):
            os.makedirs(f"{chosen_directory}/{directory}")