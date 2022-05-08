text = input().lower()
for i in "\"'.,:;!?":
    text = text.replace(i, ' ')

words = dict()

for i in text.split():
    words[i] = text.split().count(i)
try:
    print(words[input()])
except KeyError:
    print(0)
