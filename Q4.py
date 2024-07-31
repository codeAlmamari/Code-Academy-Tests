# Sample input
inputs = [2, 1, 5, 6, 2, 3]

# Validate the input
for i in inputs:
    # Check if the input is a digit
    if not isinstance(i, int):
        print('Invalid input (must be a number)')
        exit()

# Function to calculate the largest rectangle space
def largest_rectangle(inputs):
    largest = 0
    for i in inputs:
        for j in range(1 , i+1):
            length = 1
            for h in inputs[inputs.index(i)+1:]:
                if j <= h :
                    length += 1
                else:
                    break
            if largest < length * j:
                largest = length * j

    return largest

# Calculate and print the largest rectangle space
largest = largest_rectangle(inputs)
print(f'The largest rectangle is: {largest}')