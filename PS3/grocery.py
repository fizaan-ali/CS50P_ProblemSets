grocery = {}

while True:
    try:
        item = input().upper()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    except (EOFError, KeyError):
        break

grocery = dict(sorted(grocery.items()))

for item in grocery:
    print(grocery[item], item)
