import click
from sorting import remove_empty_directories


@click.command()
@click.option('--remove-empty-dirs', is_flag=True, help='Remove empty directories')
@click.option('--path', default=".", help='Provide path for sorting')
def run(path, remove_empty_dirs):
    if remove_empty_dirs:
        print("Removing empty directories...")
        remove_empty_directories(path)

if __name__ == '__main__':
    run()