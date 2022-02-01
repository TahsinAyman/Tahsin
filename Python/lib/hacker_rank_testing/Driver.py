import subprocess


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


def run():
    file = open('InputFile.txt').readlines()
    output = open('ActualOutput.txt', 'w')
    input_file = []
    for i in file:
        i = i.strip().split()
        for y in i:
            input_file.append(int(y))

    subprocess.check_call(["python", "Task.py"], stdout=output)


if __name__ == '__main__':
    run()
    test()
