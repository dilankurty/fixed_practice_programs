# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"Bigger number: {num1}")
elif num2 > num1:
    print(f"Bigger number: {num2}")
else:
    print("Equal")