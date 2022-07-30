import os
import shutil

path_to_sorting = input("Insert path: ")


def clean_empty_directories(chosen_directory):
    for directory in os.listdir(chosen_directory):
        if len(os.listdir(f"{chosen_directory}/{directory}")) == 0:
            os.rmdir(f"{chosen_directory}/{directory}")
        else:
            pass


def setup_directories(chosen_directory):
    expected_directories = ["Others", "Zips", "Text", "Video", "Execs", "Image"]
    for directory in expected_directories:
        if not os.path.exists(f"{chosen_directory}/{directory}"):
            os.makedirs(f"{chosen_directory}/{directory}")


def sort_files(chosen_directory):
    for file in os.listdir(chosen_directory):
        if file.endswith((".jpg", ".png", ".jpeg", ".gif", ".webp")):
            shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/Image")
        elif file.endswith(".exe"):
            shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/Execs")
        elif file.endswith((".webm", ".mp4", ".mov")):
            shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/Video")
        elif file.endswith((".odt", ".pdf", ".txt")):
            shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/Text")
        elif file.endswith((".rar", ".7z", ".zip")):
            shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/Zips")
        else:
            if os.path.isfile(f"{chosen_directory}/{file}"):
                shutil.move(f"{chosen_directory}/{file}", f"{chosen_directory}/Others")


setup_directories(path_to_sorting)
sort_files(path_to_sorting)
clean_empty_directories(path_to_sorting)
