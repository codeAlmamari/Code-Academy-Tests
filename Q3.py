"""
Abdulrahman Al-Mamari
Full Stack Developer Trainee on Code Academy

Day 3 solving code problem's

Q3: Given the list of numbers that presenting the heighet of each unit in the list. We have to get the best 
highet og the list, knowing that we can sum 2 units to gather if will be bigger but this 2 units must be near each other.

Algorithem:
    1. Initialize Variables:
   - Create a list `heights` containing the values to be processed.
   - Initialize a variable `bigest` to store the largest value found, set it to 0 initially.
   - Initialize a variable `num` to 0, which will be used as an index to traverse the list.

    2. Traverse the List:
    - While `num` is less than the length of `heights`:
        a. If the current value `heights[num]` is greater than `bigest`, update `bigest` to `heights[num]`.
        b. Increment `num` by 1.

    3. Output the Result:
    - Print the value of `bigest`.

    Pseudocode:
    1. Initialize heights to [2, 1, 5, 6, 2, 3]
    2. Set bigest to 0
    3. Set num to 0

    4. While num < length of heights:
        a. If heights[num] > bigest:
            i. Set bigest to heights[num]
        b. Increment num by 1

    5. Print biggest
"""

heights = [2, 1, 5, 6, 2, 3]

bigest = 0
num = 0

while num < len(heights):
    if num < len(heights) - 1:
        sum = 0
        if heights[num] > heights[num + 1]:
            sum = heights[num + 1] + heights[num + 1]
            if sum < heights[num]:
                if heights[num] > bigest:
                    bigest = heights[num]
            else:
                if sum > bigest:
                    bigest = sum
        else:
            sum = heights[num] + heights[num]
            if sum < heights[num + 1]:
                if heights[num + 1] > bigest:
                    bigest = heights[num + 1]
            else:
                if sum > bigest:
                    bigest = sum
    else:
        if heights[num] > bigest:
            bigest = heights[num]

    num += 1

print(bigest)



