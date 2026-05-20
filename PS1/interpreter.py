expression = input("Expression: ")

a, op, b = expression.split(" ")
a = int(a)
b = int(b)
match op:
    case "+":
        print(round(float(a+b),1))
    case "-":
        print(round(float(a-b),1))
    case "*":
        print(round(float(a*b),1))
    case "/":
        if b != 0:
            print(round(float(a/b),1))
        else:
            print("Denominator can't be zero brother!")
    case _:
        print("Wrong values")



