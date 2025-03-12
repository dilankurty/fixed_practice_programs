# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

number_list = []

for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    number_list.append(number)

print(f"Sum: {sum(number_list)}")
