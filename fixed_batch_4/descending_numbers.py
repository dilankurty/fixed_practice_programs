# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
        num_list.sort(reverse = True)
    except ValueError:
        print(num_list)
        break