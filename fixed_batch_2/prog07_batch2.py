# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

nums = []
even_num = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

for num in nums:
    if num%2 == 0:
        even_num += 1

print(f"Even numbers: {even_num}")
