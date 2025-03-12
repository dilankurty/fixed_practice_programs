# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

start = min(num1, num2)
stop = max(num1, num2)
num_between = []

if stop - start < 2:
    print("There are no numbers between them.")

else:
    for num in range(start + 1, stop):
        num_between.append(num)
    print(num_between)
