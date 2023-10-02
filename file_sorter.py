import os
import shutil

target_folder = input("Enter the target folder path: ")

# Create an empty dictionary to store extensions and their corresponding destination folders
extension_destinations = {}

# Iterate over all files in the source folder
for root, dirs, files in os.walk(target_folder):
    for file in files:
        # Split the file name into name and extension
        _, file_extension = os.path.splitext(file)
        
        # Add the extension to the dictionary if it's not already there
        if file_extension not in extension_destinations:
            destination = input(f"Enter the destination folder for files with extension '{file_extension}': ")
            extension_destinations[file_extension] = destination

# Print the list of unique file extensions and their corresponding destinations
print("File Extensions and Their Destinations:")
for ext, dest in extension_destinations.items():
    print(f"Extension: {ext}, Destination: {dest}")

# Move files to their respective destination folders
for root, dirs, files in os.walk(target_folder):
    for file in files:
        _, file_extension = os.path.splitext(file)
        source_file = os.path.join(root, file)
        destination_folder = extension_destinations.get(file_extension, None)
        
        if destination_folder:
            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            destination_file = os.path.join(destination_folder, file)
            shutil.move(source_file, destination_file)

print("Files have been moved to their specified destination folders.")
