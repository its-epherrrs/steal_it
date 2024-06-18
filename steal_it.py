import os
import subprocess
from pathlib import Path

# path to the file containing the URLs using %USERPROFILE%
user_profile = os.getenv('USERPROFILE')
url_file_path = Path(user_profile) / "urls" # change this if you'd rather put the urls file somewhere else

if not url_file_path.is_file():
    print(f"The file {url_file_path} does not exist.")
    exit(1)

with url_file_path.open() as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    if url:
        command = f"rip url {url}"
        print(f"Executing: {command}")
        subprocess.run(command, shell=True)

# beets moment
import_choice = input("Do you want to import the downloaded files using beets? (y/n): ").strip().lower()

if import_choice == 'y':
    config_file_path = Path(os.getenv('APPDATA')) / "streamrip" / "config.toml"
  
    if not config_file_path.is_file():
        print(f"The config file {config_file_path} does not exist.")
        exit(1)

    with config_file_path.open() as config_file:
        lines = config_file.readlines()
        path_to_import = lines[2].strip()

    if path_to_import.startswith('folder ='):
        path_to_import = path_to_import.split('=', 1)[1].strip().strip('"')

    path_to_import = path_to_import.replace('\\\\', '\\').replace('\\', '/')

    beets_command = f"beet import {path_to_import}"
    subprocess.run(beets_command, shell=True)

# add recursive to order files for VirtualDJ so that it's easier to browse
def process_order_file(file_path):
    try:
        # Try to open the file with utf-8 encoding
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            # If utf-8 fails, open the file with latin-1 encoding
            with open(file_path, 'r', encoding='latin-1') as file:
                lines = file.readlines()
        
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if '||recurse' not in line:
                    line = line.strip() + '||recurse\n'
                file.write(line)
        print(f"Processed {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_music_directory(music_directory):
    for root, _, files in os.walk(music_directory):
        for file in files:
            if file == "order":
                file_path = os.path.join(root, file)
                process_order_file(file_path)

if __name__ == "__main__":
    user_input = input("Do you want to update order files for recursive view in VirtualDJ? (y/n): ").strip().lower()
    
    if user_input == 'y':
        # Locate the user's music directory
        user_profile_music_path = os.path.expandvars(r'%userprofile%\music') # change this if VirtualDJ library is located elsewhere
        process_music_directory(user_profile_music_path)
    else:
        print("Process terminated by user.")
