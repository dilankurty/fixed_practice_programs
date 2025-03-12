# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

num_list = []
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num in num_list:
        pass
    else:
        num_list.append(num)

print(num_list)