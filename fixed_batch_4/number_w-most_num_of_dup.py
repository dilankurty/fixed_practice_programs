# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        most_duplicate = max(num_list, key = num_list.count)
        print(f"Most duplicate: {most_duplicate}")
        break