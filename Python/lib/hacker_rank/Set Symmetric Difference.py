n = int(input())
eng = set(int(i) for i in input().split())
b = int(input())
fre = set(int(i) for i in input().split())

result = eng.symmetric_difference(fre)
print(len(result))
