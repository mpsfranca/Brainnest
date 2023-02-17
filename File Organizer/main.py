import os
import shutil

FILES_FOLDER = os.path.join(os.getcwd(),"src")

def main():
    for file in os.listdir(FILES_FOLDER):
        file_path = os.path.join(FILES_FOLDER,file)
        if not os.path.isdir(file_path):
            file_extension = file.split(".")[1]
            destination_folder = os.path.join(FILES_FOLDER,f"{file_extension}")
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(file_path,destination_folder)

main()