import click
from sorting import remove_created_empty_directories, remove_empty_directories, sort_files, setup_directories

@click.command()
@click.option('--path', default=".", help='Provide path for sorting')
@click.option('--remove-empty-dirs', is_flag=True, help='Remove empty directories')
@click.option('--remove-created-empty-dirs', is_flag=True, help='Remove empty directories created by setup-dirs')
@click.option('--setup-dirs', help='Setup directories needed for sorting')
@click.option('--sort', help ='Sort files in current directory or one provided as path')
def run(path, sort, remove_empty_dirs, remove_created_empty_dirs, setup_dirs):
    if remove_empty_dirs:
        print("Removing empty directories...")
        remove_empty_directories(path)
    if remove_created_empty_dirs:
        print("Removing empty directories...")
        remove_created_empty_directories(path)
    if setup_dirs:
        print("Setting up directories...")
        setup_directories(path)
    if sort:
        print("Sorting...")
        sort_files(path)

if __name__ == '__main__':
    run()