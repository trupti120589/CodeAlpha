import os
import shutil

def organize_files(directory):
    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file extension
        file_extension = file.split('.')[-1]
        folder_name = os.path.join(directory, file_extension)

        # Create a new folder for the file extension if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Move the file to the new folder
        shutil.move(os.path.join(directory, file), os.path.join(folder_name, file))

# Example usage
directory_path = 'C:/Users/maheshmangaonkar/Desktop/Python'
organize_files(directory_path)
