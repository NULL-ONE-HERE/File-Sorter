import os
import shutil

def sort_files(source_folder, destination_folder_1, destination_folder_2, destination_folder_3):
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        
        if filename.startswith("main"):
            destination = os.path.join(destination_folder_1, filename)
        elif filename.startswith("alt"):
            destination = os.path.join(destination_folder_2, filename)
        elif filename.startswith("done"):
            destination = os.path.join(destination_folder_3, filename)
        else:
            continue  # Skip files that don't match the specified criteria
        
        shutil.move(source_file, destination)
        print(f"Moved {filename} to {destination}")

# Example usage
dump_folder = "dump"
folder_one = "main"
folder_two = "alt"
folder_three = "done"

sort_files(dump_folder, folder_one, folder_two, folder_three)
