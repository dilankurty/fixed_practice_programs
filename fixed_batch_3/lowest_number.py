# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        print(f"Lowest number: {min(num_list)}")
        break