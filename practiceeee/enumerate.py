students = ['Fizaan', 'Ans', 'Ali']

# for student in students: # now there's no indexing inside what if we want indexing

# for i in range(len(students)): # this is the way
#     print(i+1, students[i])

for i, student in enumerate(students): # enumerate(students) gives us a tuple of list like this [(0, 'Fizaan'), (1, 'Ans'), (2, 'Ali')]
    print(i+1, student)

