def sorting(lst: list):
    print('Before: ', lst)
    lst.sort()
    print('After', lst)


if __name__ == '__main__':
    with open('InputFile.txt', 'r') as input_file:
        file = input_file.readlines()
        for i in file:
            input_text = [int(_) for _ in i.split()]
            sorting(input_text)
