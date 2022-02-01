with open('shakespeare-hamlet.txt', 'r') as file:
    word = []
    for _ in range(int(input())):
        word.append(input().lower())
    test = file.read().strip().replace('\n', ' ').lower()

    count = []
    for y in word:
        count.append(test.count(y))

    for i in count:
        print(i)
"""
5
frailty
cunning
stowed
herald
skin
"""