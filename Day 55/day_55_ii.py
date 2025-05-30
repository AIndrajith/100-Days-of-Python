# Extracting meta data

import os 
from mutagen import File

def scan_directory(directory, extentions = ('.mp3','.flac','.wav')):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extentions):
                music_files.append(os.path.join(root, file))
    return music_files

def extract_metadata(file_path):
    try:
        audio = File(file_path, easy= True)
        return {
            "title": audio.get("title", ["Unknown Title"]),
            "artist": audio.get("artist", ["Unknown Artist"]),
            "album" : audio.get("album", ["Unknown Album"]),
            "genre": audio.get("genre", ["Unknown Genre"])
        }
    except Exception as e:
        print(f"Error extracting metadata for {file_path}: {e}")
        return None

directory = "Music"
files = scan_directory(directory)
print(f"Found {len(files)} music files.")

metadata = extract_metadata(files[0])
print(metadata)