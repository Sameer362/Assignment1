import os
import sys
from datetime import datetime
import shutil

print(sys.argv)


def add_timestamp_to_filename(filename):
    base, extension = os.path.splitext(filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{base}_{timestamp}{extension}"

def copy_folder_with_timestamp(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for root, dirs, files in os.walk(source_folder):
        # Create destination path
        dest_dir = root.replace(source_folder, destination_folder, 1)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(dest_dir, file)
            
            # If the file already exists in the destination, add a timestamp
            if os.path.exists(destination_file):
                destination_file = os.path.join(dest_dir, add_timestamp_to_filename(file))
            
            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} to {destination_file}")


if __name__ == "__main__":
    source = sys.argv[1]
    destination = sys.argv[2]
    copy_folder_with_timestamp(source_folder=source, destination_folder=destination)