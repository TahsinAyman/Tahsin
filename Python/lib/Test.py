from threading import Thread

def pillow_pass(n):
    lst = [_ for _ in range(1, n+1)]
    while True:
        if len(lst) == 1:
            return lst[0]

if __name__ == '__main__':
    pass
