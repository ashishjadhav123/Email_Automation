import os

path = r"C:\Users\jadha\PycharmProjects\Python_course"

for folder, sub_folders, files in os.walk(path):
    print("Folder is: ", folder)

    for sub_folder in sub_folders:
        print("Sub Folders are: ", sub_folder)

    for file in files:
        print("Files are: ", file)