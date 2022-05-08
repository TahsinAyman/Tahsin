n = int(input())
eng = set(int(i) for i in input().split())
b = int(input())
fre = set(int(i) for i in input().split())

result = eng.intersection(fre)
print(len(result))
