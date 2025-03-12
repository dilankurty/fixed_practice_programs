# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

num_list = []
while True:
    num = float(input("Enter a number: "))
    num_list.append(num)
    average = sum(num_list) / len(num_list)
    print(f"Average: {average}")