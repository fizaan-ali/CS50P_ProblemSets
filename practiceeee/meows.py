# for _ in range(3):
#     print("Meow")

# # like if there's some constants in our file it would be better to declare them constans and put them upwards so to clarify


# # now it is not constant but it is convention to put uppercase that's indicate that it is constant don't change it -> in other languages we can
# MEOWS = 3 # if ever gonna change change here only

# for _ in range(MEOWS):
#     print("meow")

# # class Cat:
# # # also there's convention in class if there's class variable that's constant 
# #     MEOWS = 3

# #     def meow(self):
# #         for _ in range(Cat.MEOWS):
# #             print("Meow")


# # cat = Cat()

# # cat.meow()

# Type Hints in python 0> tell functions to expect or return that datatype
# python doesn't care that these are always true they may be not
# bcz if we somehow wrongly type the typehint the program is gonna work find 

# mypy meows.py -> checks errors for typehints...
# def meow(n: int) -> str:
#     """Meow n times""" # a docstring
#     return n * "Meow\n"

# number: int = int(input("Number: ")) # we can also do here
# meows: str = meow(number)
# print(meows, end='')

# docstrings -> for formal documentation inside function telling what it is about
# it's imp because there are various tools for that to extract and use that docstrings to create a documentation or some other function
# also it has some formatting thing also

def meow(n: int) -> str: 
    # one of the popular convention to document a function not enforced in python
    # imp bcz we don't have to document separately just use tool and made from here
    
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int 
    :return: A string of n meows, one per line
    :rtype: str
    """
    return n * "Meow\n"

number: int = int(input("Number: ")) 
meows: str = meow(number)
print(meows, end='')