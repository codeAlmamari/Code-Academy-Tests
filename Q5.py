# Sample array
array = [2, 1, 1, 2]

# Validate the array
for i in array:
    # Check if the input is a digit
    if not isinstance(i, int):
        print('Invalid input (must be a number)')
        exit()

# Initialize a list to store the visited points
points = []

# Initialize the direction (1 = North, 2 = South, 3 = West, 4 = East)
direction = 1

# Initialize the starting point (0, 0)
x = 0
y = 0
current = [x, y]
points.append(current)  # Save the starting point

# Move and save the visited points
for i in array:
    if direction == 1:
        # Move North
        for j in range(i):
            x += 1
            current = [x, y]
            points.append(current)
        direction = 2

    elif direction == 2:
        # Move South
        for j in range(i):
            y -= 1
            current = [x, y]
            points.append(current)
        direction = 3

    elif direction == 3:
        # Move West
        for j in range(i):
            x -= 1
            current = [x, y]
            points.append(current)
        direction = 4

    elif direction == 4:
        # Move East
        for j in range(i):
            y += 1
            current = [x, y]
            points.append(current)
        direction = 1

# Check if there is a cross section
for point in points:
    # If a point is visited more than once, there is a cross section
    if points.count(point) > 1:
        print('Crossing = True')
        exit()

# If no cross section is found, print False
print('Crossing = False')