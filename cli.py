from typing_extensions import Required
import click
import sys
from sorting import remove_empty_directories


@click.command()
@click.option('--remove-empty-dirs', is_flag=True, help='Remove empty directories')
@click.option('--path', required=True, help='Provide path for sorting')
def run(path, remove_empty_dirs):
    if remove_empty_dirs:
        print("Removing empty directories...")
        remove_empty_directories(path)

if __name__ == '__main__':
    run()