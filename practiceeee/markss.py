students = [
    {"name": "Fizaan", "cgpa": 3.71},
    {"name": "Ans", "cgpa": 3.09},
    {"name": "Bilal", "cgpa": 2.05},
    {"name": "Tayyab", "cgpa": 2.95},
]

# above_3 = [
#     student['name'] for student in students if student['cgpa'] >= 3
# ]

# for student in sorted(above_3):
#     print(student)


def is_above3(s):
    return s["cgpa"] >= 3


above_3 = filter(is_above3, students)  # filter contains the conditional function..
# above_3 = filter(lambda s: True if s['cgpa'] >= 3 else False, students) we can also use the lambda function here also
# above_3 = filter(lambda s: s['cgpa'] >= 3, students) 
# returns dict the same type as in our iterable

for student in above_3:
    print(student["name"])


# black markss.py -> python code formatter