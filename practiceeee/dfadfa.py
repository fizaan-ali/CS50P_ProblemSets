# with open("names.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(',') # for csv file split it using comma
#         # print("Name:", row[0])
#         # print("CGPA:", row[1])
#         name, cgpa = line.rstrip().split(',')
#         print("Name:",name)
#         print("CGPA:",cgpa)
        
# students = []

# with open('names.csv') as file:
#     for line in file:
#         name, cgpa = line.rstrip().split(',')
#         # student = {}
#         # student['name'] = name
#         # student['cgpa'] = cgpa
#         student = {'name':name, 'cgpa':cgpa}
#         students.append(student)

# def get_name(student):
#     return student['name']
# def get_cgpa(student):
#     return student['cgpa']

# for student in sorted(students, key=get_cgpa, reverse=True):
#     print("Name",student['name'])
#     print("CGPA:",student['cgpa'])

# students = {
#         'Fizaan' : 3.71,
#         'Ans' : 3.09,
#         'Abdullah' : 3.11,
#         'Farhan' : 2.08
#     }

# def give_cgpa(item):
#     return item[1]

# for student, cgpa in sorted(students.items(), key=give_cgpa, reverse=True):
#         print(f"{student} has a cgpa of {cgpa}")

students = []
with open('names.csv') as file:
    for line in file:
        name, cgpa = line.rstrip().split(',')
        student = {'name' : name, 'cgpa' : cgpa}
        students.append(student) # list of dictionaries
    
# now we are going to use the lambda function 
# anonymous function have no name lambda x : x[1] 
# first one is the argument and the second one is the return value

for student in sorted(students, key=lambda student : student['cgpa'], reverse=True):
    print(f"{student['name']} has a cgpa of {student['cgpa']}")