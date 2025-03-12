# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

nums = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    nums.append (num)

odd_nums = 0
for num in nums:
    if num%2 != 0:
        odd_nums += 1

print(f"Odd numbers: {odd_nums}")