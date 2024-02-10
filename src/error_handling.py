def handle_loop_response(response):
    """
    Handle the user response for continuing the loop.

    Parameters:
        response (str): User input for continuing the loop.

    Returns:
        bool: True if the loop should continue, False otherwise.

    Raises:
        ValueError: If the response is neither 'y' nor 'n'.
    """
    # Checking if the response is 'n' (no)
    if response.lower() == 'n':
        return False
    # Checking if the response is 'y' (yes)
    elif response.lower() == 'y':
        return True
    # Raising an exception for invalid response
    else:
        raise ValueError("\nInvalid response. Please enter 'y' or 'n'\n")


def handle_option_response(option):
    """
    Handle the user response for choosing an option.

    Parameters:
        option (str): User input for choosing an option.

    Returns:
        str: The chosen option ('1' or '2').

    Raises:
        ValueError: If the response is neither '1' nor '2'.
    """
    # Checking if the option is '1' or '2'
    if option == '1' or option == '2':
        return option
    # Raising an exception for invalid option
    else:
        raise ValueError("\nInvalid response. Please enter '1' or '2'\n")
