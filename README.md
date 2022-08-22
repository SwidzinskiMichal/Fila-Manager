# File Manager
- Function creates directories and designated path and sorts a set of files into their acording folders.
## Description
- Program works on three functions. The setup_directories function that creates a six directories. The sort_files function that takes a list of extensions and their assigned folders and allocates the files accordingly. The folders being: Image (.jpg, .png, .jpeg, .gif, .webp.), Execs (.exe), Video (.webm, .mp4, .mov.), 
Text (.odt, .pdf, .txt.), Zips (.rar, .7z, .zip) and Other (remaining unassigned extensions). Finally clean_empty_directories function removes any empty foldes from the provided path including ones that were created by the setup_directories function but were not used.
## Getting Started
### Config File
The config.json is a file used to recognize which of the extensions are assigned to which folders as well as which folders should be created in case of any of them missing.  The modifications to the config.json have to be kept in a proper dictionary format 

{
  "Example_Image_Folder":[".jpg", ".png", ".jpeg", ".gif", ".webp"]
}

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