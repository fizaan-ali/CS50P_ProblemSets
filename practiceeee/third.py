for i in range(3):
    print("Meow")

# now in the above case we are not using the i variable but  it is required for loop so in that case 
# where we don't want that variable so in pythonic way we can just define it as _ because we don't need that in any other wy

for _ in range(3):
    print("Meow") # _ is a variable we can still use it


print("meow\n" * 3)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0: # checks whether number is positive or not
            break
    return n

# list of dictionaries
students = [
    {"name":"Fizaan", "age":12, "gpa":3.71},
    {"name":"Ans", "age":None, "gpa":3.09},
    {"name":"Usman","age":20, "gpa":3.45}
]

for student in students:
    for data in student:
        print(data, student[data],sep=" : ")
    print()


# camel case -> name, firstName, firstSecondName
# snake case -> name, first_name, first_second_name

