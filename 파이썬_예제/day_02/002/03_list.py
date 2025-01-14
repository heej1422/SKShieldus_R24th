import os

dir_path = "001"
all_files = os.listdir(dir_path)
txt_files = []

for file in all_files:
    if file.endswith('.txt'):
        print(file)
        txt_files.append(file)

        