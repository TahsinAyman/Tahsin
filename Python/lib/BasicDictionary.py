def key_to_value(dic: dict, key):
    return dic[key]


def value_to_key(dic: dict, value):
    return list(dic.keys())[list(dic.values()).index(value)]

