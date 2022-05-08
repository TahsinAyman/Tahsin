output = str()
phone = input('Phone: ')
d = dict()

digit_mapping = {
    '1': 'One',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}

for ch in phone:
    output += digit_mapping[ch] + " "

print(output)
