def swap_case(s):
    result = str()

    for i in s:
        if i == i.lower():
            i = i.upper()
            result += i
        elif i == i.upper():
            i = i.lower()
            result += i
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
