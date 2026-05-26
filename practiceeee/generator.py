def main():
    n = int(input("What's n? "))

    for s in sheep(n):
        print(s)
    

# def sheep(n): # now if we do this function for 1000000 times it's not gonaa work there is not enough ram and cpu available for this  kind of work

#     flock = []
#     for i in range(n):
#         flock.append("🐏" * i )
#     return flock    

# instead we keeps printing sidewise one by one 
# yeild turns function into generator instead of returning all value in one it instead returns  one value at a time 
def sheep(n):
    for i in range(n):
        yield "🐏" * i 
    

if __name__ == '__main__':
    main()

