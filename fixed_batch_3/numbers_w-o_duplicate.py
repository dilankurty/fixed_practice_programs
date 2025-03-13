# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicates.

num_list = []
num_wo_duplicates = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

for num in num_list:
    if num_list.count(num) == 1:
        num_wo_duplicates.append(num)

print(num_wo_duplicates)