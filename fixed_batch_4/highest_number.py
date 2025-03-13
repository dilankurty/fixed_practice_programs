# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        print(f"Highest number: {max(num_list)}")
        break