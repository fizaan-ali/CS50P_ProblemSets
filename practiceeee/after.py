import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]

if not (before.endswith('.csv') and before.endswith('.csv')):
    sys.exit("Not the CSV files..")



students = []
try:
    with open(before) as file:
        reader = csv.DictReader(file) # first header row as keys
        for line in reader:
            last, first = line['name'].split(',')
            students.append({'first':first.lstrip(), 'last':last, 'house': line['house']})
except FileNotFoundError:
    sys.exit("File 1 not found")

with open(after , "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['first','last','house'])
    writer.writeheader()
    writer.writerows(students)

