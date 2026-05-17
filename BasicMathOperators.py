print("valesp7141")

# Get user information
name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

# Get two whole numbers
num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

# Perform calculations
multiplication = num1 * num2
division = num1 / num2
subtraction = num1 - num2

# Display calculation results
print(f"Multiplication result: {multiplication:.2f}")
print(f"Division result: {division:.2f}")
print(f"Subtraction result: {subtraction:.2f}")

# Compare the numbers
if num1 > num2:
    print("The first number is larger than the second number.")
elif num1 < num2:
    print("The first number is smaller than the second number.")
else:
    print("Both numbers are equal.")

# Display user information
print(f"Name: {name}")
print(f"Student ID: {student_id}")
