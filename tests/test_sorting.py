import os
from sorting import sort_files

def test_sorting(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["Image", "Video"])
    create_files(filenames=["example.jpeg", "example.mp4"])

    # act
    sort_files(tmp_path)

    # assert
    assert os.path.exists(f"{tmp_path}/Image/example.jpeg")
    assert not os.path.exists(f"{tmp_path}/example.jpeg")

    assert os.path.exists(f"{tmp_path}/Video/example.mp4")
    assert not os.path.exists(f"{tmp_path}/example.mp4")


def test_sorting_fail(tmp_path, create_directories, create_files):
    # arrange
    create_directories(dirnames=["ExecsFail", "SongsFail"])
    create_files(filenames=["example.exe", "example.mp3"])

    # act
    sort_files(tmp_path)

    # assert

    assert not os.path.exists(f"{tmp_path}/ExecsFail/example.exe")
    assert not os.path.exists(f"{tmp_path}/SongsFail/example.mp3")
