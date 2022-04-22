import csv

with open('data.csv') as file:
    csv_reader = list(csv.reader(file, delimiter='-'))
    print(csv_reader)
    with open('new_data.csv', 'w') as write_file:
        csv_write = csv.writer(write_file, delimiter=',')
        csv_write.writerows(csv_reader)
