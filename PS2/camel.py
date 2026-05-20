# program to convert from camel case to snake case
# name -> name, firstName -> first_name

variable = input("camel case: ")

# firstName -> first_name
print("snake case: ", end="")
for c in variable:
    if c.isupper():
        print(f"_{c.lower()}",end="")
    else:
        print(c,end="")
