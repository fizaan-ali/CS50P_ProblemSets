while True:
    try:
        x = input("What's x? ")
    except EOFError:
        print("EOFError")
        break
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
    else:
        print(x)
        