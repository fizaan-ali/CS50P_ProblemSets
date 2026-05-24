import re

name = input("What's your name? ").strip()
  
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"hello, {name}")

matches = re.search(r"^(.+), *(.+)$", name)

# there's also parenthesis() for capturing purposes

if matches:
    # last, first = matches.groups() # returns a tuple of capturing groups
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print("hello,", name)

# diff btw matches.group() and matches.groups() 
# walrus operator := 
# it assings the value and also returns at the same expression
# like this assign and then compare with return value

# if matches := re.search(r"^(.+), *(.+)$", name):
#     print("valid")
# else:
#     print("invalid")