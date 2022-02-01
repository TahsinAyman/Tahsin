text = input().lower()
for i in "\"'.,:;!?":
    text = text.replace(i, ' ')

words = dict()
word = input()
for i in text.split():
    words[i] = text.split().count(i)

if word in list(words.keys()):
    print(words[word])
else:
    print(0)
