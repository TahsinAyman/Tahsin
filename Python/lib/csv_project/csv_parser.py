import csv
rows = header = []
with open('data.csv') as file:
<<<<<<< HEAD
    csv_reader = csv.reader(file, delimiter='-')
    # header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
    print(rows)
    with open('new_data.csv', 'w', newline="") as write_file:
        csv_write = csv.writer(write_file)
        # csv_write.writerow(header)
        csv_write.writerows(rows)
=======
    csv_reader = list(csv.reader(file, delimiter='-'))
    print(csv_reader)
    with open('new_data.csv', 'w') as write_file:
        csv_write = csv.writer(write_file, delimiter=',')
        csv_write.writerows(csv_reader)
>>>>>>> be47d96ece8ba228d90c31c18afd9a2ac7205675
