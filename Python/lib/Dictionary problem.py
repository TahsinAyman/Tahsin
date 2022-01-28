def key_to_value(dic: dict, key):
    return dic[key]


def value_to_key(dic: dict, value):
    return list(dic.keys())[list(dic.values()).index(value)]


if __name__ == '__main__':
    dic = {1: 2, 3: 4}
    print(key_to_value(dic, 1))
    print(value_to_key(dic, 2))
