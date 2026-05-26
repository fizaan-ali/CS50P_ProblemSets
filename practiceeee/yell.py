# def main():
#     yell(['This','is','CS50'])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
    
#     print(*uppercased) # unpacking list also in print

# if __name__ == '__main__':
#     main() 

# def main():
#     # yell('This','is','CS50')
#     yell("My", "name", "is", "Fizaan")

# def yell(*words): # *args -> variable
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
    
#     print(*uppercased) # unpacking
    
# if __name__ == '__main__':
#     main()

# also then there's this map function which applies function to every item in the iterable
# quite useful
# def main():
#     yell("This", "is", "cs50")

# def yell(*words):
#     uppercased = map(str.upper, words) # returns map object
#     print(*uppercased)

# if __name__ == '__main__':
#     main()

# also there's list comprehension

def main():
    yell("thiss is CS50")

def yell(*words):
    uppercased = [word.upper() for word in words] # list comprehension

    print(*uppercased)

if __name__ == '__main__':
    main()