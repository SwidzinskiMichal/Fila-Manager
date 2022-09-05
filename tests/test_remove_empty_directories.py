import os
from sorting import remove_empty_directories

def test_remove_empty_directories(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["Image"])
    create_files(filenames=["example.jpeg"])
    
    # act
    remove_empty_directories(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/example.jpeg")
    assert not os.path.exists(f"{tmp_path}/Image")