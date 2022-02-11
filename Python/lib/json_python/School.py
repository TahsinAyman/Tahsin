import json

with open('dataOfBangladeshSchools.json') as file:
    data = json.load(file)

# for i in range(len(list(data))):
#     print('School Name:', data[i]['name'])
#     print('School Place:', data[i]['place'])
#     print(f'\t{data[i]["name"]} Students')
#     for y in range(len(list(data[i]['students']))):
#         print('\t\tName: ', data[i]['students'][y]['name'], ',')
#         print('\t\tRoll: ', data[i]['students'][y]['roll'], ',')
#         print('\t\tID: ', data[i]['students'][y]['id'], ',')
#         print('\t\tClass: ', data[i]['students'][y]['class'], '\n\t\t____________________')
for y in range(len(list(data))):
    for i in data[y]['students']:
        i['phone'] = 213

with open('new_json.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)
