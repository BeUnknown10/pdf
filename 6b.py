import shutil
import os
dir = input("Enter the directory name to zip: ")
if os.path.exists(dir)==True:
    print("File exists")
    a=shutil.make_archive(dir, 'zip' ,'C:\Users\Asus\OneDrive\Desktop\AIML4cb21ai031\PYTHON\pdf\python1')
else:
    print("File does not exists")