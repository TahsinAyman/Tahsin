def task(s):
    output = []
    a = 0
    for i in s:
        if a < 0:
            break
        if i == '[':
            a += 1
        elif i == ']':
            a -= 1
    if a == 0:
        output.append('Yes')
    else:
        output.append('No')

    for i in output:
        print(i)


if __name__ == '__main__':
    with open('InputFile.txt', 'r') as input_file:
        file = input_file.readlines()
        for i in file:
            input_text = i.replace(' ', '')
            task(input_text)

