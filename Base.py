import os
import subprocess
import time
import hashlib
from datetime import datetime ,date
import sys




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




