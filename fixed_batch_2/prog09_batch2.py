# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

nums = []

for i in range(101):
    if i%5 != 0:
        nums.append(i)

print(nums)