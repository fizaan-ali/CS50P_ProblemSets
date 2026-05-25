class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Cookie capacity can't be negative")
        self._capacity = n

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, n):
        if not 0 <= n <= self.capacity:
            raise ValueError("Behold the invalid number of cookies")
        self._size = n
def main():
    jar = Jar()
    jar.deposit(3)
    print("Size:",jar.size)
    print("Capacity:", jar.capacity)
    # jar.deposit(14) -> value error
    jar.withdraw(2)
    print("Size:",jar.size) # now size is 1
    jar.deposit(10)
    print(jar)
    # jar.withdraw(20) -> value error


if __name__ == '__main__':
    main()
