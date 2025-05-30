# Scanning directory

import os 

def scan_directory(directory, extentions = ('.mp3','.flac','.wav')):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extentions):
                music_files.append(os.path.join(root, file))
    return music_files

directory = "Music"
files = scan_directory(directory)
print(f"Found {len(files)} music files.")