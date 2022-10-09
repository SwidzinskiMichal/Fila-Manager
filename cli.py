import click 
from sorting import remove_created_empty_directories, remove_empty_directories, sort_files, setup_directories
import os
import json

def check_config():
    if os.path.isfile('config.json'):
        pass
    else:
        raise Exception("Config file is required to proceed")

with open("config.json") as config_dict:
    config = json.load(config_dict)
    cli_config = config["cli_config"]

@click.command()
@click.option('--path', default=".", help='Provide path for sorting')
@click.option('--remove-empty-dirs/--dont-remove-empty-dirs', default=cli_config["remove_empty_dirs"], help='Remove empty directories')
@click.option('--remove-created-empty-dirs/--dont-created-empty-dirs', default=cli_config["remove_created_empty_dirs"], help='Remove empty directories created by setup-dirs')
@click.option('--setup-dirs/--dont-setup-dirs', default=cli_config["setup_dirs"], help='Setup directories needed for sorting')
@click.option('--sort/--dont-sort', default=cli_config["sort"], help ='Sort files in current directory or one provided as path')
def run(path, sort, remove_empty_dirs, remove_created_empty_dirs, setup_dirs):
    if remove_empty_dirs:
        print("Removing empty directories...")
        remove_empty_directories(path)
    if remove_created_empty_dirs:
        print("Removing created empty directories...")
        remove_created_empty_directories(path)
    if setup_dirs:
        print("Setting up directories...")
        setup_directories(path)
    if sort:
        print("Sorting...")
        sort_files(path)
        
check_config()
if __name__ == '__main__':
    run()