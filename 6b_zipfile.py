import shutil
import os

directory_to_zip = input("Enter the directory name to zip: ")

# Use a raw string for Windows paths
archive_base_name = r'D:\microsoft visual studio code\java'  # Change this to your desired archive location and name

# Create the zip archive
shutil.make_archive(archive_base_name, 'zip', directory_to_zip)

# Check if the archive file was created
if os.path.exists(archive_base_name + '.zip'):
    print(f"Zip archive '{archive_base_name}.zip' was created successfully.")
else:
    print(f"Zip archive '{archive_base_name}.zip' was not created.")
