import os
from sorting import sort_files

def test_sorting(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["Image", "Video", "Execs", "Songs"])
    create_files(filenames=["example.jpeg", "example.mp4", "example.exe", "example.mp3"])

    # act
    sort_files(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/Image/example.jpeg")
    assert not os.path.exists(f"{tmp_path}/example.jpeg")

    assert os.path.exists(f"{tmp_path}/Video/example.mp4")
    assert not os.path.exists(f"{tmp_path}/example.mp4")

    assert os.path.exists(f"{tmp_path}/Execs/example.exe")
    assert not os.path.exists(f"{tmp_path}/example.exe")

    assert os.path.exists(f"{tmp_path}/Songs/example.mp3")
    assert not os.path.exists(f"{tmp_path}/example.mp3")
