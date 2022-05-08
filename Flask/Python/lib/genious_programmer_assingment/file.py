'''
steps of file handling:
1. Open a file
2. Read / Write from / into file
3. Close the file

1. Open a file:
fileObjet = open("file.txt", "access-mode")
'''


# fileObj = open("file.txt", "w")
# print(fileObj)
# if fileObj:
#     print("file is opened successfully!!")
# fileObj.close()

# with open("file.txt", "r") as fileObj:
#     print("file is opened successfully!!")
#     content = fileObj.read()
#     print(content)
# \n
with open('file.txt', 'r') as f:
    content = f.readlines()
    print(content[0])
5
frailty
cunning
stowed
herald
skin

1
4
1
1
1
