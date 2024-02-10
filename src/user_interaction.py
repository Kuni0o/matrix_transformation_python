import error_handling as er


# Function used for separating each part of a code in terminal
def spacing():
    print()
    print("--------------------------------------------")
    print()


# Function used for displaying menu for a user and returning a chosen option
def check_user_input():
    # Loop until valid option is entered
    while True:
        try:
            # Displaying options for the user
            print("Choose one of the options:")
            print("1. Find the transformation matrix of an unit square based on the entered coordinates.")
            print("2. Transform an unit square based on the entered transformation matrix.")

            # Getting user input to choose an option
            option = input("Enter a number: ")
            # Handling the user's option
            er.handle_option_response(option)
            # Exiting the loop if no exceptions occurred
            break
        except ValueError as e:
            # Handling the case when the user inputs an invalid value
            print(e)
    # Returning the chosen option
    return option




