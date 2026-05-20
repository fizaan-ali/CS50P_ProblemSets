# x = int(input("What's x? "))
# y = int(input("What's y? "))

# z = x / y

# print(f"{z:.2f}") # upto 2 decimal placeee

def main():
    x = int(input("What's x? "))
    print("Square of x is: ", square(x))

def square(n):
    return n * n

main()