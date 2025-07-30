import os
import shutil

def copy_files(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    
    for filename in os.listdir(source_dir_path):
        source_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f"Copying {source_path} -> {dest_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_files(source_path, dest_path)
