import os
import shutil

# Define your paths
source_exe = r"D:\Dhanush\Python Concepts\12. Automation Projects\to be copied file.txt"
root_folder = r"D:\Dhanush\Python Concepts\12. Automation Projects\One Day data"

# Loop through everything inside the main folder
for item in os.listdir(root_folder):
    item_path = os.path.join(root_folder, item)
    
    # Check if the item is a folder
    if os.path.isdir(item_path):
        # Build the final destination path for the exe
        destination = os.path.join(item_path, os.path.basename(source_exe))
        
        # Copy the file
        shutil.copy2(source_exe, destination)
        print(f"Copied to: {item_path}")
