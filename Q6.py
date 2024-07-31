# Get the number of buildings from the user
num_buildings = int(input("Enter the number of buildings: "))

# Create a list to store the buildings
buildings = []

# Get the details of each building from the user
for i in range(num_buildings):
    left, right, height = map(int, input("Enter the left, right, and height of building {}: ".format(i+1)).split())
    buildings.append([left, right, height])

# Sort the buildings by their left edge
buildings.sort()

# Initialize the list of turn points
turn_points = [[0, 0]]

# Initialize the maximum height seen so far
max_height = 0

# Iterate over the buildings to find the turn points
for left, right, height in buildings:
    # If the current building is taller than the maximum height, add a turn point
    if height > max_height:
        turn_points.append([left, height])
        max_height = height
    # If the current building is shorter than the maximum height, add a turn point
    if height < max_height:
        turn_points.append([right, height])

# Add the final turn point
turn_points.append([right, 0])

# Print the turn points
print("The turn points are:", turn_points)