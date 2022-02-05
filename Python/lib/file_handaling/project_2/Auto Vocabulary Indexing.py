with open('vocabulary.txt') as input_file:
    letter = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13,
              'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
              'y': 25,
              'z': 26}
    text = input_file.read().strip().lower().replace('\n', ' ').split()
    result = []
    lst = []
    for i in text:
        lst.append(letter[i[0]])
    lst.sort()
    dic = dict()
    for i in text:
        dic[letter[i[0]]] = i


for i in result:
    print(i)
