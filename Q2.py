'''
Abdulrahman Al-Mamari
Full Stack Developer Trainee on Code Academy

Day 2 solving code problem's


Q2: Given the n*n 2Dmatrix representing an image rotate the image by 90 degree (clock wise)

Algorithem:
    - first we define n*n matrix 
    - get the length of the matrix
    - nested for loop to handle element by element in the matrix
    - then i use for loop to print the matrix after the rotation

to solve this problem i study how and where the position of each elements move 
and the mechanism of moving 90 degree with clockwise on n*n matrises and i end up with this.
using matrix 4*4 
matrix[j][i] = matrix[i][j+3]
matrix[j+1][i] = matrix[i][j+2]
matrix[j+2][i] = matrix[i][j+1]
matrix[j+3][i] = matrix[i][j]


'''

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

# matrix length
n = len(matrix)

# rotat the matrix element by element.
for i in range(n):
    for j in range(n):
        matrix[j][n-1-i] = matrix[i][j]

# print the rotated matrix
print()
print("Matrix after 90 degree clockwise rotation:")
for row in matrix:
    print(row)
print()


'''
we can do it in one single line using np from numpy libarary:
matrix = np.rot90(np.array(matrix), k=-1).tolist()
'''

    
