output,text = open('vocabulary.txt').read().strip().lower().split('\n')
text.sort()
for i in text:
    file.write(i + '\n') if text.index(i) != 0 else file = open('indexed vocabulary.txt', 'w')
