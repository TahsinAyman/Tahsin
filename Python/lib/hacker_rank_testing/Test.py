with open('file.txt') as file:
    for i in range(len(file.readlines())):
        if i % 2 == 0:
            txt = file.readline()
            print(txt)
