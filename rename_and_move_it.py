from mutagen.flac import FLAC
import os
import re
import shutil

def set_album_artist(file_path):
    try:
        # Load FLAC file
        audio = FLAC(file_path)
        
        # Get artist from the ARTIST tag
        artist = audio.get("artist", [""])[0]
        
        # Get album artist from the ALBUMARTIST tag
        album_artist = audio.get("albumartist", [""])[0]
        
        # Check if there is a comma in the artist or album artist tag
        if ',' in album_artist:
            # Extract artist name up to the first comma if present
            match = re.match(r'([^,]+)', artist)
            if match:
                album_artist_extracted = match.group(1).strip()
                
                # Set ALBUMARTIST tag
                audio["albumartist"] = album_artist_extracted
                
                # Save changes
                audio.save()
                
                print(f"Processed: {file_path}")
            else:
                print(f"No match found in artist tag, ignoring file: {file_path}")
        else:
            print(f"No comma in album artist tag, ignoring file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def rename_flac_files(base_directory):
    for root, _, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith(".flac"):
                file_path = os.path.join(root, filename)
                try:
                    # Load FLAC file
                    audio = FLAC(file_path)
                    
                    # Get track number and title
                    track_number = audio.get("tracknumber", [""])[0].strip()
                    track_title = audio.get("title", ["Unknown"])[0].strip()
                    
                    # Construct new filename
                    new_filename = f"{track_number} - {track_title}.flac"
                    new_file_path = os.path.join(root, new_filename)
                    
                    # Rename file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} to {new_file_path}")
                    
                except Exception as e:
                    print(f"Error renaming file {file_path}: {e}")

def move_flac_files(base_directory):
    for root, _, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith(".flac"):
                file_path = os.path.join(root, filename)
                try:
                    # Load FLAC file
                    audio = FLAC(file_path)
                    
                    # Get album artist and album name
                    album_artist = audio.get("albumartist", ["Unknown Artist"])[0].strip()
                    album_name = audio.get("album", ["Unknown Album"])[0].strip()
                    year = audio.get("year", ["Unknown Year"])[0].strip()

                    # Create target directory
                    target_directory = os.path.join(base_directory, album_artist, f"{album_name} ({year})")
                    os.makedirs(target_directory, exist_ok=True)
                    
                    # Move file to target directory
                    shutil.move(file_path, os.path.join(target_directory, filename))
                    print(f"Moved: {file_path} to {target_directory}")

                    # Move cover.jpg if it exists
                    cover_path = os.path.join(root, "cover.jpg")
                    if os.path.exists(cover_path):
                        shutil.move(cover_path, os.path.join(target_directory, "cover.jpg"))
                        print(f"Moved cover.jpg to {target_directory}")
                    
                except Exception as e:
                    print(f"Error moving file {file_path}: {e}")

def delete_empty_folders(base_directory):
    for root, dirs, _ in os.walk(base_directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                try:
                    os.rmdir(dir_path)
                    print(f"Deleted empty folder: {dir_path}")
                except Exception as e:
                    print(f"Error deleting empty folder {dir_path}: {e}")

# Prompt user to input the base directory where FLAC files are located
base_directory = input("Enter the base directory where FLAC files are located: ").strip()

# Validate if the directory exists
if not os.path.isdir(base_directory):
    print(f"Error: Directory '{base_directory}' does not exist.")
    exit()

# Iterate over FLAC files in the directory and subdirectories
for root, _, files in os.walk(base_directory):
    for filename in files:
        if filename.endswith(".flac"):
            file_path = os.path.join(root, filename)
            set_album_artist(file_path)

rename_flac_files(base_directory)
move_flac_files(base_directory)
delete_empty_folders(base_directory)