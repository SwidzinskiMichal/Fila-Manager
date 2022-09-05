import pytest
import os


@pytest.fixture()
def create_files(tmp_path, filenames = []):
    def _create_files(filenames = []):
        for filename in filenames:
            open(f"{tmp_path}/{filename}", 'w').close()
    
    return _create_files

@pytest.fixture()
def create_directories(tmp_path, dirnames = []):
    def _create_directories(dirnames = []):
        for dirname in dirnames:
          if not os.path.exists(f"{tmp_path}/{dirname}"):
            os.makedirs(f"{tmp_path}/{dirname}")
    
    return _create_directories