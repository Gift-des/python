# A class is a blueprint
# Object is an instance


class Person:

 # Properties/Attribute/Characteristic

    name = "Kash"
    age = 18
    height = 2.1

    # Method/function/behaviour

    def walk(self):
        print("Person is walking")

accountant = Person() # Creating an object
accountant.walk()