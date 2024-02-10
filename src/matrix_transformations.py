import matplotlib.pyplot as plt


def calc_matrix_cord(newMatrix, resMatrix):
    """
    Calculate the transformation matrix of a unit square.

    This function calculates the transformation matrix based on the new coordinates of a unit square
    and stores the result in the provided 'resMatrix' array.

    Parameters:
        newMatrix (list): The new coordinates of the unit square stored as a 2D array.
        resMatrix (list): An empty transformation matrix to store the result.

    Returns:
        list: The calculated transformation matrix.

    """
    # Calculating the shift vector for the first column
    resMatrix[0][0] = round(newMatrix[0][3] - newMatrix[0][0], 3)
    resMatrix[1][0] = round(newMatrix[1][3] - newMatrix[1][0], 3)

    # Calculating the shift vector for the second column
    resMatrix[0][1] = round(newMatrix[0][1] - newMatrix[0][0], 3)
    resMatrix[1][1] = round(newMatrix[1][1] - newMatrix[1][0], 3)

    # Storing the new coordinates of the point A (old (0, 0)) in the third column
    resMatrix[0][2] = round(newMatrix[0][0], 3)
    resMatrix[1][2] = round(newMatrix[1][0], 3)

    return resMatrix


def plot_square_transform(transformMatrix):
    """
    Plot the transformation of a unit square based on the given transformation matrix.

    This function calculates the new coordinates of a unit square after applying the transformation
    specified by the given transformation matrix, and then plots the transformed square.

    Parameters:
        transformMatrix (list): The transformation matrix used for transforming the unit square.

    Returns:
        None
    """
    # Initialize lists to store the x and y coordinates of the transformed square
    xCords = [0, 0, 0, 0]
    yCords = [0, 0, 0, 0]

    # Calculate the new coordinates of the four corners of the transformed square
    xCords[0] = transformMatrix[0][2]
    yCords[0] = transformMatrix[1][2]

    xCords[1] = transformMatrix[0][1] + transformMatrix[0][2]
    yCords[1] = transformMatrix[1][1] + transformMatrix[1][2]

    xCords[3] = transformMatrix[0][0] + transformMatrix[0][2]
    yCords[3] = transformMatrix[1][0] + transformMatrix[1][2]

    # Calculate the new coordinates of the point (1, 1) by finding the center of the BD diagonal
    pointA = [xCords[0], yCords[0]]
    pointB = [xCords[3], yCords[3]]
    pointD = [xCords[1], yCords[1]]
    diagonalCenter = [(pointD[0] + pointB[0]) / 2, (pointD[1] + pointB[1]) / 2]

    # Calculate the shift from point A to the center of the BD diagonal
    xDelta = pointA[0] - diagonalCenter[0]
    yDelta = pointA[1] - diagonalCenter[1]

    # Calculate the new coordinates of point C by reflecting point A across the center of the BD diagonal
    xCords[2] = diagonalCenter[0] + -xDelta
    yCords[2] = diagonalCenter[1] + -yDelta

    # Plot the x and y axes
    plt.axhline(y=0, color='black', linestyle='--')
    plt.axvline(x=0, color='black', linestyle='--')

    # Set the limits for the plot
    plt.xlim(-7, 7)
    plt.ylim(-7, 7)

    # Set aspect ratio to be equal
    plt.gca().set_aspect('equal', adjustable='box')

    # Set the title and labels for the plot
    plt.title('Transformation of a unit square')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Plot the red line connecting points (0, 0) and (0, 1)
    plt.plot([xCords[0], xCords[1]], [yCords[0], yCords[1]], color='red')

    # Plot the green line connecting points (0, 0) and (1, 0)
    plt.plot([xCords[0], xCords[3]], [yCords[0], yCords[3]], color='green')

    # Fill the area inside the transformed square with cyan color
    plt.fill(xCords, yCords, "c")

    # Display the grid
    plt.grid(True)

    # Show the plot
    plt.show()



