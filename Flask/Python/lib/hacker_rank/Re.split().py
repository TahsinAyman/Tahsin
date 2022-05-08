import re

regex_pattern = r","  # Do not delete 'r'.
string = input()

string = string.replace('.', ',')

string = string.split(',')

print(string)

for ch in string:
    print(ch)
