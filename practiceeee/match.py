name = input("What's your name? ")
# like a switch statement in c++
# match name:
#     case "Fizaan":
#         print("Shafiq")
#     case "Ali":
#         print("Shafiq")
#     case "Areeb":
#         print("Shafiq")
#     case _: # handles all other cases like default
#         print("Other")

match name:
    case "Fizaan" | "Ali" | "Areeb":
        print("Shafiq")
    case _:
        print("Other")

# not need break statement like in c++

