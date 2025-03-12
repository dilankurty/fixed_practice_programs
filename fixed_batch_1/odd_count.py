# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_list = []

for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    if number % 2 != 0:
        odd_list.append(number)

print(f"Odd count: {len(odd_list)}")