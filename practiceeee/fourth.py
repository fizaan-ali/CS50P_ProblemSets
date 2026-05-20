#syntaxx error -> can't be handled must resolve manually
# value error

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer!")
# else:
#     print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an int")
#     else:
#         break
# print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an int")


# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except:
#             pass # if you want to do nothing on here just silently handle

# main()

def main():
    y = get_int("What's y? ")
    print(f"y is {y}")

def get_int(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            pass
        

main()