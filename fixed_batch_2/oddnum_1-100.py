# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

num_list = []
num = 1
while num <= 100:
    num_list.append(num)
    num += 2

print(num_list)