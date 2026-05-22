import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
if not file_name.endswith('.csv'):
    sys.exit("Not a CSV file")

menu = []
try:
    with open(file_name) as file:
        reader = csv.reader(file)
        for line in reader: # line = list
            menu.append(line) # list of lists
except FileNotFoundError:
    sys.exit("File doesn't exist")

print(tabulate(menu, headers='firstrow', tablefmt='grid'))