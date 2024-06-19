class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is studying")

accountant = Person("Joe",34,"Male")
print(accountant.name)
print(accountant.age)
accountant.details()


consultant = Person("Martha",56,"Female")


print(consultant.gender)
print(consultant.age)


doctor = Person("John",34,"Male")
print(doctor.name)