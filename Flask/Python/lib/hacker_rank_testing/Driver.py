from subprocess import check_call as run_file


def test():
    inputFile = open('InputFile.txt').readlines()
    actual_output = open('ActualOutput.txt').readlines()
    expected_output = open('ExpectedOutput.txt').readlines()

    for i in range(len(inputFile)):
        compile = True
        try:
            actual_output[i]
        except Exception:
            print(f"Test Case {i + 1} Failed")
            compile = False
        try:
            expected_output[i]
        except Exception:
            print(f"Test Case {i + 1}: please define expected output!")
            compile = False

        if compile:
            if actual_output[i].strip() == expected_output[i].strip():
                print(f"Test Case {i + 1} Passed.")
            else:
                print(f"Test Case {i + 1} Failed")
    # actual_output = open('ActualOutput.txt', 'w')
    # actual_output.write('')


def run():
    output = open('ActualOutput.txt', 'w')
    run_file(["python", "Task.py"], stdout=output)


if __name__ == '__main__':
    run()
    test()
