# Prog05: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers with the decimal point

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
        
if num2 == 0:
    print("Cannot divide by zero.")
else:
    qoutient = num1 / num2
    print(f"Qoutient: {qoutient}")