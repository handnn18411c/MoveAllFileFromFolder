import shutil
import os
from pathlib import Path

source_dir = r"D:\MongoDB\Excel\Dot_1"
target_dir = r"C:\Users\NhatHan\Desktop\Test_Python"

list_Folder = list()
folder_names = os.listdir(source_dir)
for i in folder_names:
    list_Folder.append(i)

for string_path in list_Folder:
    folder = r"D:\MongoDB\Excel\Dot_1\{0}".format(string_path)
    file_names = os.listdir(folder)
    for file_name in file_names:
        shutil.move(
            os.path.join(folder, file_name),
            target_dir,
        )
