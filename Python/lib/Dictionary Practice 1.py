text = input()
word = input()
words = dict()

for i in text.split():
    cnt = 0
    for y in text.split():
        if i == y:
            cnt += 1
    words[i] = cnt

print(words[word])
