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
<<<<<<< HEAD:Python/lib/hacker_rank_testing/Driver.py
    file = open('InputFile.txt').readlines()
=======
    file = open('inputFile.txt').readlines()
>>>>>>> 2c730a6a345bef0d6c3e7f65a3e53e96b8c833a7:Python/lib/file_handaling/Project 1/Driver.py
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
