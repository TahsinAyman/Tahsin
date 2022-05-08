# open('copyfile.txt', 'w').write(open('file.txt', 'r').read())

with open('copyfile.txt', 'w') as wFile:
    with open('file.txt', 'r') as rFile:
        wFile.write(rFile.read())

# with open('file.txt', 'r') as copy:
#     open('copyfile.txt', 'w').write(copy.read())
