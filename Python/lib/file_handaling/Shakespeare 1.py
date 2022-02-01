with open('shakespeare-hamlet.txt', 'r') as file:
    word = []
    count = []

    for _ in range(int(input())):
        word.append(input().lower())

    text = file.read().strip().replace('\n', ' ').lower()

    for z in "[](){},.?!'\":;-":
        text = text.replace(z, '')

    for i in word:
        cnt = 0
        for y in text.split():
            if i == y:
                cnt += 1
        count.append(cnt)

    for i in count:
        print(i)
