text, word = open('shakespeare-hamlet.txt', 'r').read().strip().replace('\n', ' ').lower(), []
for _ in range(int(input())):
    word.append(input().lower())
for i in "[](){},.?!'\":;-":
    text = text.replace(i, '')
for i in word:
    print(text.strip().split().count(i))
