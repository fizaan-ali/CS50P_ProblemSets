import csv

name = input("What's name? ")
age = input("What's age? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file) # it contains csv file as argument
#     writer.writerow([name, age]) # it accepts list of argments to be added in csv file

with open('students.csv ', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name','age'])
    writer.writerow({'name':name, 'age':age})
