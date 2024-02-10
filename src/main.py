# Importing modules for error handling, user interaction, and matrix transformations
import error_handling as er
import user_interaction as ui
import matrix_transformations as mt

# Variable to control program loop
programLoop = True

# Main loop for the program
while programLoop:

    chosenOption = ui.check_user_input()

    # Option 1: Find the transformation matrix of a unit square
    if chosenOption == '1':
        # Initializing a new matrix to store new coordinates of the unit square
        newCordMatrix = [[0, 0, 0, 0], [0, 0, 0, 0]]
        # Initializing a default transformation matrix
        defResMatrix = [[0, 0, 0], [0, 0, 0], [0.000, 0.000, 1.000]]

        ui.spacing()

        print("Enter square coordinates AFTER transformation\n")

        # Loop for filling the new coordinates of the unit square
        for i in range(0, 4):
            cordLoop = True
            if i == 0:
                while cordLoop:
                    try:
                        print("Enter new (0, 0) coordinates")
                        newCordMatrix[0][i] = float(input("x: "))
                        newCordMatrix[1][i] = float(input("y: "))
                        print()
                        cordLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')
            if i == 1:
                while cordLoop:
                    try:
                        print("Enter new (0, 1) coordinates")
                        newCordMatrix[0][i] = float(input("x: "))
                        newCordMatrix[1][i] = float(input("y: "))
                        print()
                        cordLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')
            if i == 2:
                while cordLoop:
                    try:
                        print("Enter new (1, 1) coordinates")
                        newCordMatrix[0][i] = float(input("x: "))
                        newCordMatrix[1][i] = float(input("y: "))
                        print()
                        cordLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')
            if i == 3:
                while cordLoop:
                    try:
                        print("Enter new (1, 0) coordinates")
                        newCordMatrix[0][i] = float(input("x: "))
                        newCordMatrix[1][i] = float(input("y: "))
                        print()
                        cordLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')

        # Calculating the transformation matrix
        toPrintMatrix = mt.calc_matrix_cord(newCordMatrix, defResMatrix)

        ui.spacing()

        print("Transformation matrix:\n")
        # Printing a transformation matrix using for loop
        for i in range(0, 3):
            print(f"[{toPrintMatrix[i][0]} {toPrintMatrix[i][1]} {toPrintMatrix[i][2]}]")

    # Option 2: Transform a unit square based on the entered transformation matrix
    elif chosenOption == '2':
        # Initializing a transformation matrix
        transformationMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]

        ui.spacing()

        print("Enter a transformation matrix of an unit square\n")

        # Loop for filling the transformation matrix
        for i in range(0, 3):
            matLoop = True
            if i == 0:
                while matLoop:
                    try:
                        print(f"Enter {i + 1}. column")
                        transformationMatrix[0][i] = float(input("First row: "))
                        transformationMatrix[1][i] = float(input("Second row: "))
                        print()
                        matLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')
            if i == 1:
                while matLoop:
                    try:
                        print(f"Enter {i + 1}. column")
                        transformationMatrix[0][i] = float(input("First row: "))
                        transformationMatrix[1][i] = float(input("Second row: "))
                        print()
                        matLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')
            if i == 2:
                while matLoop:
                    try:
                        print(f"Enter {i + 1}. column")
                        transformationMatrix[0][i] = float(input("First row: "))
                        transformationMatrix[1][i] = float(input("Second row: "))
                        print()
                        matLoop = False
                    except ValueError:
                        print('\nInvalid input. Please enter a number\n')
        mt.plot_square_transform(transformationMatrix)

    ui.spacing()

    # Asking the user if they want to continue the program
    while True:
        try:
            loopAns = input("Continue?[y/n] ")
            programLoop = er.handle_loop_response(loopAns)
            break
        except ValueError as e:
            print(e)

    ui.spacing()
