# Automating the Backup Process with Timestamps

import os
import shutil
from datetime import datetime

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def copy_file(source, destination):
    shutil.copy2(source, destination)

def create_backup_directory(base_backup_dir):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(base_backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

def backup_files(source_dir, backup_dir):
    files = list_files(source_dir)
    for file in files: 
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(backup_dir, file)
        copy_file(source_path, destination_path)
        print(f"Backed up: {file}")