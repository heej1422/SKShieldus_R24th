import os

dir_path = "001"
all_files = os.listdir(dir_path)
txt_files = []

for file in all_files:
    if file.endswith('.txt'):
        print(file)
        txt_files.append(file)

# 디렉토리 내의 txt 파일을 하나씩 불러와서 오픈
for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    #print(file_path)

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())

        