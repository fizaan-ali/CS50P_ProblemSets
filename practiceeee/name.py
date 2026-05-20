# command line arguments take arguments while commanding

import sys

#sys.argv gives the list of the things written in command line
# for item in sys.argv:
#     print(item)

# print("Hello,", sys.argv[1])

# try:
#     print("Hello,", sys.argv[1])
# except IndexError:
#     print("Too few index!")

# if  len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello,", sys.argv[1])


if  len(sys.argv) < 2:
    sys.exit("Too few arguments") # terminate the program after printing this lien
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("Hello,", sys.argv[1])

