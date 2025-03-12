# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)

        if num_list.count(num) == 1:
            print("Unique")
        else:
            print("Duplicate")
    
    except ValueError:
        break