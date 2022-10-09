import os
from sorting import setup_directories

def test_setup_dirs(tmp_path):

    # act
    setup_directories(tmp_path)    
    
    # assert    
    assert os.path.exists(f"{tmp_path}/Image")
    assert os.path.exists(f"{tmp_path}/Video")
    assert os.path.exists(f"{tmp_path}/Execs")
    assert os.path.exists(f"{tmp_path}/Songs")

def test_setup_dirs_fail(tmp_path):

    # act
    setup_directories(tmp_path)    
    
    # assert    
    assert not os.path.exists(f"{tmp_path}/ImageFail")
    assert not os.path.exists(f"{tmp_path}/VideoFail")
    assert not os.path.exists(f"{tmp_path}/ExecsFail")
    assert not os.path.exists(f"{tmp_path}/SongsFail")
