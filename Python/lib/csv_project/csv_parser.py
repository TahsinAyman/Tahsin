import csv

with open('data.csv') as file:
    data = csv.reader(file)
    next(data)

    # for line in data:
    #     print(line)

    with open('new_data.csv', 'w') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',')

        for line in data:
            csv_writer.writerow(line)
