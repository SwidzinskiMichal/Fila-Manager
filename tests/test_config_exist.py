import os

def test_config_exist():
    if os.path.isfile('config.json'):
        pass
    else:
        raise Exception("Config file is required to proceed")