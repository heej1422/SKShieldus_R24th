with open('example.txt', 'r', encoding='utf-8') as hellofile:
    content = hellofile.readlines()
    for line in content:
        print(line, end='')