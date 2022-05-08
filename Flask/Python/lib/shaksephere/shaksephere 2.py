with open('file.txt', 'r') as file:
    line_no = 1
    document = dict()
    for line in file.readlines():
        document[line_no] = line.replace('\n', '')
        line_no += 1
    input_text = dict()
    line_no = 1
    n = input()
    input_text[line_no] = n
    cnt = 0
    while True:
        cnt += 1
        if len(n) > 0:
            line_no += 1
            n = input()
            input_text[line_no] = n
        else:
            break
    input_text.pop(line_no)
    cereal_number = []
    for i in input_text:
        for y in document:
            if input_text[i] == document[y]:
                if document[i] == document[i + list(document.keys())[i + 1]]:
                    cereal_number.append(y)
                else:
                    cereal_number = []

    print(cereal_number)
