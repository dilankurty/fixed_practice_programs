# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

num_list = []
for i in range(10):
    num = float(input("Enter a number: "))
    num_list.append(num)

duplicates = []
for num in num_list:
    if num_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)