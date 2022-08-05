import os
from sorting import sort_files, setup_directories

def test_sorting(tmp_path):
    # arrange
    setup_directories(tmp_path)

    files_to_create = ["example.jpeg", "example.mp4", "example.exe"]
    for filename in files_to_create:
        open(f"{tmp_path}/{filename}", 'w').close()
    
    # act
    sort_files(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/Image/example.jpeg")
    assert not os.path.exists(f"{tmp_path}/example.jpeg")

    assert os.path.exists(f"{tmp_path}/Video/example.mp4")
    assert not os.path.exists(f"{tmp_path}/example.mp4")

    assert os.path.exists(f"{tmp_path}/Execs/example.exe")
    assert not os.path.exists(f"{tmp_path}/example.exe")
