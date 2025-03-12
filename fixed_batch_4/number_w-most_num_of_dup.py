# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

num_list = []
while True:
    num = float(input("Enter a number: "))
    num_list.append(num)

    most_duplicate = max(num_list)
    print(f"Most duplicate: {most_duplicate}")