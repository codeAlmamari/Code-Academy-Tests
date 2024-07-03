"""
Q : Giving the 2 integers black and white representing the count of the colored balls (return the maximum high for the triangle).
"""

"""

Solution: 


Abdulrahman Abdullah Al-Mamari
Web development course

Algorithm:
    - The program starting with tacking the numbers of the black and white balls
    - The line is a variable that saving the number of lines in each iteration 
    - counterJ is telling the number of White balls in each line
    - counterI is telling the number of Black balls in each line
    - The we have Wile loop  continues if there are enough balls for the next required
    - The first if statment check if the white balls enough for the first row of the triangle 
    - the next if statment check if there is enough Balck balls for the second row and so on 

"""


# let the user enter the number of white ball.
white = int(input("Enter the number of White balls (j): "))
# let the user enter the number of black ball.
black = int(input("Enter the number of Black balls (i): "))

    
line = 0        # number of lines we have
counterJ = 1    # number of white ball required for first row
counterI = 2    # number of black ball required for second row

while white >= counterJ or black >= counterI: 
    # check the white ball if enough for the line 
    if white >= counterJ:
       line += 1
       white -= 2
       counterJ += 2
    else:
        break
    # check the black ball if enough for the line 
    if black >= counterI:
        line += 1
        black -= 2 
        counterI += 2

# print the number of lines with given balls.
print("output", line)
