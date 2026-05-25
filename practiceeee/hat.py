import random
# class Hat:
#     def __init__(self):
#         self.houses = ['Gryffindor', 'Slytherin', 'RavenClaw']

#     def sort(self, name):
#         house = random.choice(self.houses)
#         print(name, "is in", house )
# # now in this scenario houses is instance variables it's gonna instantiate and take space every time an object is created and if not object is created there is no houses


# hat = Hat()
# hat.sort("Harry")


# now we wanna make a class that's only a container and not allow that to instantiate objects bcz we don't need them
class Hat:
    # class variable belongs to class
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw'] 

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# now hat is a class method we can access it via class name

Hat.sort('Harry')