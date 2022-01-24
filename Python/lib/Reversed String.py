def reversed_string(string):
    s = str()
    for i in range(len(string) - 1, -1, -1):
        s += string[i]
    return s


if __name__ == '__main__':
    print(reversed_string(input('Enter String: ')))
