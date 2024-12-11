def new_section():
    new_line = "-" * 79
    print(new_line)
    print('\n')

def menu():
    while True:
        new_section()
        choice=input('1. Display Iris dataset features.\n2. Display Iris dataset target variable.\n3. Print Iris dataset keys.\n4. Proceed to model training and results.\n\nPlease choose an option:')
        if int(choice) == 1:
            return 1
        elif int(choice) == 2:
            return 2
        elif int(choice) == 3:
            return 3
        elif int(choice) == 4:
            return 4
        print('Please choose a valid option')
        
