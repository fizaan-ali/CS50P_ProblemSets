# # from sixth import square

# # def main():
# #     test_square()

# # def test_square():
# #     # if square(2) != 4:
# #     #     print("2 squared was not 4")
# #     # if square(3) != 9:
# #     #     print("3 squared was not 9")
# #     try:
# #         assert square(2) == 4 # assert means that it should that the boolean expression after assert should be true otherwise it's gonna throw an error
# #     except AssertionError:
# #         print("2 sqaured was not 4")

# #     try:
# #         assert square(3) == 9
# #     except AssertionError:
# #         print("3 squared was not 9")

# #     try:
# #         assert square(-2) == 4
# #     except AssertionError:
# #         print("-2 squared was not 4")

# #     try:
# #         assert square(-3) == 9
# #     except AssertionError:
# #         print("-3 squared was not 9")

# #     try:
# #         assert square(0) == 0
# #     except AssertionError:
# #         print("0 squared was not 0")

# #     # test some cases and edge cases 




# # if __name__ == '__main__':
# #     main()

# # # assert keyword



# # now using pytest

# from sixth import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0
    
# # pytest test_sixth.py
# # also it stops at if it meets first assertion failure in that funct

import pytest
from sixth import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
