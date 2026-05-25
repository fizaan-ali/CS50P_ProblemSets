class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

# by the following method we can call the get function without any need of object need
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

# chicken in the egg problem 
def main():
    student = Student.get()
    print(student)

if __name__ == '__main__':
    main()