# import csv
# boys = []

# with open("addresses.csv") as file:
#     reader = csv.reader(file) # gives us tupless
#     for name, home in reader: # row = list of our comma separated values in one line
#         boys.append({"name": name, "home": home})
        

# print(boys) # list of dictionaries

# for boy in sorted(boys, key=lambda boy: boy['name']):
#     print(f"{boy['name']} lives in {boy['home']}")

import csv

students = []

with open('addresses.csv') as file:
    reader = csv.DictReader(file) # gives us dictionaries with keys = headers
    for row in reader:
        students.append({"name" : row['name'], "home" : row['home']})
        # print(row) # dict

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} lives in {student['home']}")
