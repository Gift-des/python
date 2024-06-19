temperature = 32

if temperature < 25:
    print("It is cold")

elif temperature > 25:
    print("It is hot")

else:
    print("Normal Temperature")

# A PROGRAM THAT RETURNS THE LARGEST NUMBER AMONG THREE NUMBERS
first = 56
second = 23
third = 78
if first > second and first > third:
    print(first, "the largest number")

elif second > first and second > third:
    print(second, "the largest number")

else:
    print(third, "the largest number")

# A Python Program to determine whether a number is even or odd
num = 0

if num == 0:
    print(num, "is neutral")
elif num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# A Python Program that returns the area of a rectangle
# A=L * W
length = 20
width = 5
area = length * width
print(area)
print("The area is ", area)

# A Python Program that returns the area of a trapezium

a = 30
b = 20
h = 5
area = (a+b*h)/2
print(area)
print("The area is ", area)



