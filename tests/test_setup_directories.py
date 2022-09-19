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
