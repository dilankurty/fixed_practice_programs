# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
        
if num1 < num2:
    print(f"Smaller number: {num1}")
elif num2 < num1:
    print(f"Smaller number: {num2}")
else:
    print("Equal.")