from Task import add


def test():
    actual_output = open('ActualOutput.txt').readlines()
    expected_output = open('ExpectedOutput.txt').readlines()

    if len(actual_output) != len(expected_output):
        print('Compilation Error!')
        exit("Try Again")
    for i in range(len(expected_output)):
        if actual_output[i].strip() == expected_output[i].strip():
            print(f"Test Case {i + 1} Passed.")
        else:
            print(f"Test Case {i + 1} Failed")


if __name__ == '__main__':
    file = open('inputFile.txt').readlines()
    output = open('ActualOutput.txt', 'w')
    input_file = []
    for i in file:
        i = i.strip()
        i = i.split()
        for y in i:
            input_file.append(int(y))
    for z in range(0, len(input_file) - 1, 2):
        result = add(input_file[z], input_file[z + 1])
        output.write(str(result) + "\n")
    output.close()
    test()
