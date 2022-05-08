import csv

with open("data.csv") as file:
    data = csv.reader(file)
print(data)
