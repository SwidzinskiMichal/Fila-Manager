import os
from sorting import setup_directories

def test_setup_dirs(tmp_path):

    # act
    setup_directories(tmp_path)    
    
    # assert    
    assert os.path.exists(f"{tmp_path}/Image")
    assert os.path.exists(f"{tmp_path}/Video")


def test_setup_dirs_fail(tmp_path):

    # act
    setup_directories(tmp_path)    
    
    # assert    
    assert not os.path.exists(f"{tmp_path}/ImageSetupFail")
    assert not os.path.exists(f"{tmp_path}/VideoSetupFail")

