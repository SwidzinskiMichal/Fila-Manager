import os
import shutil
import json
from pathlib import Path


with open("config.json") as config_dict:
    file_categories = json.load(config_dict)


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


def setup_directories(chosen_directory):
    expected_directories = list(file_categories.keys())    
    for directory in expected_directories:
        if os.path.exists(f"{chosen_directory}/{directory}"):
            pass
        else:
            os.makedirs(f"{chosen_directory}/{directory}")