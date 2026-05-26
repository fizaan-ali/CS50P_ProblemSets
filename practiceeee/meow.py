# import sys

# if len(sys.argv) == 1:
#     print("Meow")
# elif len(sys.argv) == 3 and sys.argv[1] == '-n':
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("Meow")
# else:
#     print("usage: meows.py")
# it is going to turn really messy to check and maintain the sequence and allotment of various thing like -a, -s, -x, etc...abs with sys library


# argparse library

import argparse

parser = argparse.ArgumentParser(description= "Meow like a cat") # description of program
parser.add_argument("-n", default=1, type= int, help= "number of times to meow") 
# set some help statment while doing -h or --help, also take default values like if there's no -n values given and also specify the type of that arguments
args = parser.parse_args()
+
# python meow.py -h

for _ in range(args.n):
    print("Meow")

# it's convention to use single hypen with single digit and -- with words
# e.g. -n, -a, -s, or --name, --size, --help
