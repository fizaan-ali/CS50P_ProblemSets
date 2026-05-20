# x = int(input("What's x? "))
# y = int((input("What's y? ")))
# if x < y:
#     print("x is less than y")
# if x > y: 
#     print("x is greater than y")
# if x == y:
#     print("x equals y")

# score = int(input("Score: "))
# now there can be three version each one better of previous one

# if(score>=90 and score<=100):
#     print("Grade: A")
# elif(score>=80 and score < 90):
#     print("Grade: B")
# elif(score>=70 and score < 80):
#     print("Grade: C")
# elif(score>=60 and score < 70):
#     print("Grade: D")
# else:
#     print("Grade: F")

# if 90 <= score <=100: # we can nest the two conditions**
#     print("Grade: A")
# elif 80<= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# and now the third one as python interprets the code line by line so we implicitly knows the upper range 
# if score >= 90:
#     print("Grade: A")
# elif score >= 80: # here it implicitly knows the range is at the 89 because above 90 is already checked above
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")   

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# the above lines of code can be written as
# def is_even(n):
#     return True if n % 2 == 0 else False


def is_even(n):
    return (n % 2 == 0)