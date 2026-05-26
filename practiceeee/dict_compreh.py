students = ['Fizaan', 'Ans', 'Ali'] 

# marks = []

# for student in students:
#     marks.append({'name':student, 'cgpa':3})

# marks = [{'name':student, 'cgpa':3} for student in students] # list comprehension for each iteration add the dict

# now create big dict with student name: student cgpa

marks = {student : 3 for student in students} # dictionary comprehension

print(marks)