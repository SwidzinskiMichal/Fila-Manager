import os
import shutil 
from sorting import remove_empty_directories, remove_created_empty_directories

def test_remove_empty_directories(tmp_path, create_directories):
    # arrange
    create_directories(dirnames=["TestDir"])
    
    # act
    remove_empty_directories(tmp_path)

    # assert
    assert not os.path.exists(f"{tmp_path}/TestDir")

def test_fail_remove_empty_directories(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["Image"])
    create_files(filenames=["example.jpeg"])
    shutil.move(f"{tmp_path}/example.jpeg",f"{tmp_path}/Image")

    # act
    remove_empty_directories(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/Image")

def test_remove_created_empty_directories(tmp_path, create_directories):
    # arrange
    create_directories(dirnames=["Image"])
    
    # act
    remove_created_empty_directories(tmp_path)

    # assert
    assert not os.path.exists(f"{tmp_path}/Image")

def test_fail_remove_created_empty_directories(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["ImageRemoveFail"])
    create_files(filenames=["example.jpeg"])
    # act
    remove_created_empty_directories(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/example.jpeg")
    assert os.path.exists(f"{tmp_path}/ImageRemoveFail")