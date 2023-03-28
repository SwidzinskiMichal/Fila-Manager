from cli import check_config

def test_config_exist():
    assert check_config('config.json') == True
    
def test_config_doesnt_exist():
    assert check_config('config_example.json') == False