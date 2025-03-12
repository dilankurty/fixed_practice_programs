# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

num_list = []
for i in range(101):
    if i%5 != 0:
        num_list.append(i)

print(num_list)