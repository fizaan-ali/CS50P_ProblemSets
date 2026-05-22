# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print("Hello,", name)

# name = input("What's your name? ")

# file = open("names.txt", "w") # open the file 'names.txt' to write
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# w -> erases the entire content of the file if there is 

# with open("names.txt", "a") as file: # no need to manually close the file
#     file.write(f"{name}\n")

# read from file 
# with open("names.txt", "r") as file:
    # lines = file.readlines() # returns list of all lines of the file

# print(type(lines))
# print(lines)
# for line in lines:
    # print(line, end="")
    # print(line.rstrip())

# we can directly do this to iterate over  all lines in file

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# names = []
# with open("names.txt") as file: # by default read
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}")

# or simply using sorted() function on file

# with open("names.txt") as file:
#     for line in sorted(file, reverse=True): # by default reverse is false
#         print(f"Hello, {line.rstrip()}")

# file = open("names.txt")
# lines = file.readlines() # returns a list of all lines in a file
# print(lines)
# file.close()

