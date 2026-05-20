# print("My name is 'Fizaan'.")
# print("My name is \"Fizaan\"")
# name = input("What's your name? ");
# print(f"My name is {name}.")

# print("Fizaan", "Ali", "Shafiq", sep='yo', end='haha')

# name = input("What's your name? ").strip().title()

#removes whitespace from string
# name = name.strip() # function /method 
#capitalize user's name
# name = name.capitalize()

# name = name.title()


# now we can chain functions inside python
# name = name.strip().title()


# print(f"Hello {name}")

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print("Hello,", to)

main()