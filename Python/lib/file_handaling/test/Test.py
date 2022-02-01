with open('file.txt', 'r') as file:
    word = []
    for _ in range(int(input())):
        word.append(input())
    test = file.read().strip().replace('\n', ' ')
    count = []
    print(test)
    for y in word:
        cnt = 0
        for i in test.strip().split():
            if y == i:
                cnt += 1
        count.append(cnt)
    print(count)

