# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    num_list.append(num)

difference = num_list[0] - sum(num_list[1:])
print(difference)