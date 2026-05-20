import random

def main():
    correct = 0
    level = get_level()
    x = []; y = []
    for i in range(10): # now it generates us 10 x and y random integers of level size
        x.append(generate_integer(level))
        y.append(generate_integer(level))

    for i in range(10):
        count = 0
        for j in range(3):
            try:
                sum = int(input(f"{x[i]} + {y[i]} = "))
            except ValueError:
                print("EEE")
                count+=1
                if count == 3:
                    print(f"{x[i]} + {y[i]} = {x[i]+y[i]}")
                continue

            if sum == x[i] + y[i]:
                if j == 0:
                    correct+=1
                break
            else:
                print("EEE")
                count+=1
                if count == 3:
                    print(f"{x[i]} + {y[i]} = {x[i]+y[i]}")

    print("Score: ", correct)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == '__main__':
    main()

