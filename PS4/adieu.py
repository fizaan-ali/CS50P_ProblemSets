from inflect import engine

p = engine()

names = []

while True:
    try:
        name = input("Name: ").title()
    except EOFError:
        break
    else:
        names.append(name)

if len(names) != 0:
    line = p.join(names)

    print("Adieu, adieu, to", line)
