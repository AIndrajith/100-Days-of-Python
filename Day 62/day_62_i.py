# Handling File Operations in Python

import os
import shutil

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def copy_file(source, destination):
    shutil.copy2(source, destination)