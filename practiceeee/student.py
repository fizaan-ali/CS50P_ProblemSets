# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
    
#     return name, house # returns a tuple not two variables or values but tuple of two values
# #   return (name, house) # explicitly say return a tuple
# #   return [name, house] # now this returns explicit list
# #   return {"Name":name, "House":house} # returns dict with keys and values
# if __name__ == '__main__':
#     main()

# class Student:
#     ...
 

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == '__main__':
#     main()

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name") # or raise ValueError
#         if house not in ['Satellite', 'Model', 'Professor']:
#             raise ValueError("Not my type")
#         self.name = name 
#         self.house = house

#     def __str__(self): # whenever we print object it's gonna execute this function also like __init__ 
#         return f"{self.name} from {self.house}"
 

# def main():
#     student = get_student()
#     # print(f"{student.name} from {student.house}")
#     # now as we've done error checking in __init__ we can still be able to change by following 
#     # self.house = 'something' there's no stopping of it
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")

#     return Student(name, house) # we can also use try and except block here to handle the ValueError if happens as we've mentioned in the class


# if __name__ == '__main__':
#     main()

class Student:
    def __init__(self, name, house):
        # now with getters and setters there's no need for error checing in here
        # if not name:
        #     raise ValueError("Missing name") # or raise ValueError
        # if house not in ['Satellite', 'Model', 'Professor']:
        #     raise ValueError("Not my type")
        self.name = name 
        self.house = house

    def __str__(self): # whenever we print object it's gonna execute this function also like __init__ 
        return f"{self.name} from {self.house}"
 
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not Name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ['Satellite','Model','Professor']:
            raise ValueError("Invalid house")

        self._house = house

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    # now as we've done error checking in __init__ we can still be able to change by following 
    # self.house = 'something' there's no stopping of it
    
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")

    return Student(name, house) # we can also use try and except block here to handle the ValueError if happens as we've mentioned in the class


if __name__ == '__main__':
    main()

# now after doing setter there's no need for error checking in __init__ because in init whenever we are initializing it's going to set the value through the same setter function

# as property (getter and setter) can't have same name as our oiginal variable or attribute so we put _ underscore besides our original variables 
# to somehow differentiate between the two and we access our variables via the properties which are getter and setter functions we can still access our variable publicly using _variable..abs

