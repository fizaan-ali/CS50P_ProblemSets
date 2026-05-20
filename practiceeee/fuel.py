def main():
    fraction = input("Input: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        
        if x < 0 or y < 0 or x > y:
            raise ValueError
        
        percentage = (x/y) * 100

    except ValueError:
        # print("ValueError")
        raise
    except ZeroDivisionError:
        # print("ZeroDivisionError")
        raise
    else:
        return round(percentage)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == '__main__':
    main()