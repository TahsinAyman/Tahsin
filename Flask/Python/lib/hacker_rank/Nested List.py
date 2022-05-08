if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_min = minint = 1000000.5
    for record in records:
        if record[1] < minint:
            second_min = minint
            minint = record[1]
        elif second_min > record[1] != minint:
            second_min = record[1]
    output = ([record[0] for record in records if record[1] == second_min])
    output.sort()
    for x in output:
        print(x)
