# While Loop
# increment
number = 20
while number <= 25:
    print(number)
    number += 1

num = 105
while num <= 110:
    print("number is", num)
    num += 1

# decrement
count = 10
while count >= 1:
    print(count)
    count -= 1

# break and continue statement
x = 25
while x <= 30:
    print(x)
    if x == 27:
        break
    x += 1

b = 0
while b <= 5:
    b += 1
    if b == 3:
        continue
    print(b)


# For loop
for y in range(7):
    print(y)

for z in range(40, 45):
    print(z)

for mynumber in range(100, 110, 3):
    print(mynumber)


languages = ['Python', 'Java', 'C++', 'Javascript']
for lang in languages:
    print(lang)



