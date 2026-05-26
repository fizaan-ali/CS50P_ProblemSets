# # global variable -> read in any function / can't write without telling the function that it's global with 'global' variable.  local to module
# local variable -> can be accessed and changed only in that function other functions can't have access to it 

# balance = 0 


# def main():
#     print("Balance:", balance)

# if __name__ == '__main__':
#     main()

# balance = 0

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == '__main__':
#     main()

# but can't write directly global variable directly 
# we need to tell the function that this variable is global with the 'global' keyword

# Pythons' scope resolution -> LEGB (local, enclosed, global, built-in)
# python access variables in this fashion  


class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)
    

if __name__ == '__main__':
    main()