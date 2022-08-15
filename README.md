# File Manager
- Function creates directories and designated path and sorts a set of files into their acording folders.
## Description
- Program works on three functions. The setup_directories function that creates a six directories. The sort_files function that takes a list of extensions and their assigned folders and allocates the files accordingly. The folders being: Image (.jpg, .png, .jpeg, .gif, .webp.), Execs (.exe), Video (.webm, .mp4, .mov.), 
Text (.odt, .pdf, .txt.), Zips (.rar, .7z, .zip) and Other (remaining unassigned extensions). Finally clean_empty_directories function removes any empty foldes from the provided path including ones that were created by the setup_directories function but were not used.
## Getting Started
### Config File
The config_extensions.txt is a file used to recognize which of the extensions are assigned to which folders. The config_dicts.txt is a folder possessing a list of folders that will be created. The modifications to the config_extensions.txt have to be kept in a proper dictionary format 
{
  "Name_Of_Folder":[".extensions", ".assigned", ".to", ".folder"],
  "Example_Image_Folder":[".jpg", ".png", ".jpeg", ".gif", ".webp"]
}

If a new folder is added it needs to be present both in config_extensions.txt and config_dicts.txt, otherwise the config_dicts.txt will not provide the information to create a folder or config_extensions.txt will not know what files should be assigned to created folder.
Folder names in config_dicts.txt should be provided like this:

Others,Zips,Text,Video,Execs,Image

Without spaces between them, separated by comma.

### Setup
This project is using Makefile. To see all available commands run:
```
make

help                           Shows a list of commands with short descriptions
install                        Installs project requirements
setup                          Setup project
venv                           Setup venv in a current directory
test                           Run tests
```
### Dependencies
- Python 3.8
- Make 
- Additional requirements in requirements.txt
### Authors
- Michał Świdziński