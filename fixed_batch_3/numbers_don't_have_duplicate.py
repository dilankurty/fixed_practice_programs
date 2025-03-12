# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicates.

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

print(num_list)