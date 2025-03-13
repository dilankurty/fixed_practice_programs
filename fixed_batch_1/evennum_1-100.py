# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

even_numbers = []

for num in range(101):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)