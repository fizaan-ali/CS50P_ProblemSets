import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue


target = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess <= 0:
        continue
    if guess > target:
        print("Too large!")
        continue
    elif  guess < target:
        print("Too small!")

    else:
        print("Just right!")
        break
