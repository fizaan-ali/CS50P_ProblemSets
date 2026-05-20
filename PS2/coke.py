amount_due = 50
while True:
    print("Amount Due:", amount_due)
    insert_coin = int(input("Insert Coin:"))
    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        amount_due = amount_due - insert_coin
        if amount_due <= 0:
            print("Change Owed:", -(amount_due))
            break

