# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
number_list = []
for num in range(101):
    if num % 10 != 0:
        number_list.append(num)

print(number_list)