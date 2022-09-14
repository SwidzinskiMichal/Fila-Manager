import os
from sorting import remove_created_empty_directories

def test_remove_created_empty_directories(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["Image", "Test_Dir"])
    create_files(filenames=["example.jpeg"])
    
    # act
    remove_created_empty_directories(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/example.jpeg")
    assert os.path.exists(f"{tmp_path}/Test_Dir")
    assert not os.path.exists(f"{tmp_path}/Image")
    