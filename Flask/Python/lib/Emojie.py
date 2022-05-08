
output = str()
message = input('>: ')
message.split(' ')

emojie = {
    '(:': '😊',
    '):': '😢'
}

for w in word:
    output += emojie.get(w, w)

print(output)
print(' My brother is a bhogdel')