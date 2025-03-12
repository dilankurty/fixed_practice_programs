# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

nums = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    nums.append (num)

print(f"Sum: {sum(nums)}")
