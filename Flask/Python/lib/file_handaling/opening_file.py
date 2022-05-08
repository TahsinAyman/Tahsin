f = open('file.txt', 'r')
text = f.read()
print(text, end='')

f.close()

f = open('file.txt', 'a')
f.write(input() + '')

f.close()
