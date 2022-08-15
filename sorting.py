from distutils.command.config import config
import os
import json
import shutil
from pathlib import Path


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


def setup_directories(chosen_directory):
    for directory in expected_directories:
        if os.path.exists(f"{chosen_directory}/{directory}"):
            pass
        else:
            os.makedirs(f"{chosen_directory}/{directory}")