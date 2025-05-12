import os
import subprocess
import time
import hashlib
from datetime import datetime ,date
import sys


password = 

os.environ["RCLONE_CONFIG_PASS"] = password




def get_recent_files(directory, cutoff_time):
    recent_files = []
    for root, _, files in os.walk(directory):
  
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = os.path.getmtime(file_path)
          
            if modified_time > cutoff_time:
                recent_files.append(file_path)
    return recent_files


def check_for_changes(files_to_upload, remote_path, rclone_remote): 
    """Checks for changes in the local directory and uploads updated files."""

    try:

        
        if files_to_upload:
          print("Changes detected. Uploading...")
          for file_path in files_to_upload:
            relative_path = os.path.relpath(file_path, local_directory)  
            remote_file_path = f"{remote_path}/{relative_path}" 
            
            print(f"Uploading {file_path} to {remote_file_path}")

            try:
                subprocess.run(
                    ["/home/s5708799/Downloads/rclone/rclone", "copyto", file_path, f"{rclone_remote}:{remote_file_path}"],
                    env=os.environ,
                    check=True
                )
                print(f"Uploaded: {file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error uploading {file_path}: {e}")
        else:
            print("No changes detected.")

    except Exception as e:
        print(f"An error occurred: {e}")


test = sys.argv[0]
print(test)
    


    
