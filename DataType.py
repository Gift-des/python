# Datatype

number = 60  # Int
num = 45.36  # Float
greeting = "Hello there"  # str
isPythonInteresting = True  # boolean
fruits = ["apple", "banana"]  # list
cars = ("BMW", "Audi")  # Tuple-index position can't change
countries = {"Kenya", "Tanzania"}  # Set-unordered
student = {
    "firstname": "Gold",
    "age": 19,
    "course": "MiT"
}  # Dictionary
print(num)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])
print(student["age"])

# Determining data type

print(type(isPythonInteresting))
print(type(cars))
print(type(student))

# Typecasting is converting one datatype to another.

print((int(num)))
print(float(number))
