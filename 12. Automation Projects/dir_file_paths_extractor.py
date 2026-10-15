import os

dir_path = r"C:\Users\user\Desktop\playground\merging ppts\azi45"
file_paths = []

for root, dirs, files in os.walk(dir_path):   
    for file in files:
        
        # Combine the directory path and file name
        full_path = os.path.join(root, file)
        file_paths.append(full_path)


print(file_paths)
