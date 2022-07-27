import os
import shutil


path = input("Insert path: ")


def folders(path):
    if not os.path.exists(f"{path}/Image"):
        os.makedirs(f"{path}/Image")
    if not os.path.exists(f"{path}/Execs"):
        os.makedirs(f"{path}/Execs")
    if not os.path.exists(f"{path}/Video"):
        os.makedirs(f"{path}/Video")
    if not os.path.exists(f"{path}/Text"):
        os.makedirs(f"{path}/Text")
    if not os.path.exists(f"{path}/Zips"):
        os.makedirs(f"{path}/Zips")
    if not os.path.exists(f"{path}/Others"):
        os.makedirs(f"{path}/Others")


def sorting(path):
    for file in os.listdir(path):
        if file.endswith(".jpg") or file.endswith(".png"):
            shutil.move(f"{path}/{file}", f"{path}/Image")
        elif file.endswith(".exe"):
            shutil.move(f"{path}/{file}", f"{path}/Execs")
        elif file.endswith(".webm") or file.endswith(".mp4") or file.endswith(".mov"):
            shutil.move(f"{path}/{file}", f"{path}/Video")
        elif file.endswith(".odt") or file.endswith(".pdf"):
            shutil.move(f"{path}/{file}", f"{path}/Text")
        elif file.endswith(".rar") or file.endswith(".7z") or file.endswith(".zip"):
            shutil.move(f"{path}/{file}", f"{path}/Zips")
        else:
            if os.path.isfile(f"{path}/{file}"):
                shutil.move(f"{path}/{file}", f"{path}/Others")


folders(path)
sorting(path)
