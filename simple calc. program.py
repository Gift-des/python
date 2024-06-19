
print("Select Operations")
print(
    "1. Addition",
    "2. Subtraction",
    "3. Multiplication",
    "4. Division")

# Giving the option to the user to choose the operation

operation = int(input("Enter choice of operation 1/2/3/4: "))

# Taking Input from the Users

num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

# Apply Conditional Statements: To make operation as-per-user choices

if operation == 1:
    print(num1, "+", num2, "=", (num1, num2))

elif operation == 2:
    print(num1, "-", num2, "=", (num1, num2))

elif operation == 3:
    print(num1, "*", num2, "=", (num1, num2))

elif operation == 4:
    print(num1, "/", num2, "=", (num1, num2))

else:
    print("Invalid Input")
