import csv
rows = header = []
with open('data.csv') as file:
    csv_reader = csv.reader(file, delimiter='-')
    # header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
    print(rows)
    with open('new_data.csv', 'w', newline="") as write_file:
        csv_write = csv.writer(write_file)
        # csv_write.writerow(header)
        csv_write.writerows(rows)
