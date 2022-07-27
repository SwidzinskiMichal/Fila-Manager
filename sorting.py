import os
import shutil


def sorting():
    path = input("Insert path: ")
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
                shutil.move(f"{path}/{file}", f"{path}/EE")


sorting()