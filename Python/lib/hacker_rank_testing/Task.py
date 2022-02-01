def add(var1: int, var2: int):
    print(f'{var1} + {var2} = {var1 + var2}')


if __name__ == '__main__':
    with open('InputFile.txt', 'r') as input_file:
        file = input_file.readlines()
        for i in file:
            input_text = [int(_) for _ in i.split()]
            add(input_text[0], input_text[1])
