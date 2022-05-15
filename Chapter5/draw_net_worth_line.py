# coci20c2p1

# Draw a line that represents the net worth of the company over
# a period of n days.
#
# For each of the n days, Josip he knows if the net worth of his company
# increased by one unit (+), decreased by one unit (-), or remained the 
# same (=) during that day. Before the first day, the net worth was == 0.
#
# Josip will draw the line in a big infinite matrix of characters. 
# Indices of matrix rows grow upwards, and indices of columns grow to
# the right. 
# For the i-th day he will draw some character in the i-th column
#
# The character and the index of the row are decided by the following
# rules:
# 
# -If the net worth increased during the i-th day, he will draw '/' in
#   the row with index equal to the net worth at the beginning of the day
# -If the net worth decreased during the i-th day, he will draw '\' in 
#   the row with index equal to the net worth at the end of the day
# -If the net worth didn't change during the i-th day, he will draw '_'
#   in the row with index equal to the net worth during the day. 
# -All other cells are filled with '.' 
#
# Your task is to output the minimal matrix that contains the whole
# line, i.e. contains all characters /, \, and _ that Josip drew
#
# Input:
# First line, n == number of days
# Second line a string of n characters +, -, =, that represent how the
# company's net worth changed over the given period
# Output:
# The described matrix

# Plan: 
# 1. Iterate thru the inputs and find the "coordinates" 
#    for each symbol, making a list of lists holding two ints each.
# 2. Use the X coordinates to find the "frame," i.e., number
#    of rows, difference between min and max, inclusive
# 3. Add to each Y value a number that would make the min
# 4. Y value 0
# 5. Set up a list of lists to represent the grid.
# 6. Iterare thru the coordinate lists to populate the grid
# 7. Print the grid. 

# collect the number of columns
cols = int(input())
# collect the sequence and translate the characters to what will be drawn
inpt = input()
seq = ''
for char in inpt:
    if char == '-':
        seq += '\\'
    if char == '=':
        seq += '_'
    if char == '+':
        seq += '/'

# Create a list of coordinates, the index of each set will correspond to the index
# of each character in the seq string created above
coordinates = []
x = None
for i in range(cols):
    if x == None:
        x = 0
    # two negatives ('\') in a row will take the image down a row
    if i > 0 and seq[i-1] == '\\' and seq[i] == '\\':
        x -= 1
    # two consec positives ('/'), or a positive ('/') and an equal ('_')
    # will take the image up a row
    if i > 0 and seq[i-1] == '/' and (seq[i] == '/' or seq[i] == '_'):
        x += 1
    # If the previous column was equal and the current column is negative ('\')
    # move the image down a row 
    if i > 0 and seq[i-1] == '_' and seq[i] == '\\':
        x -= 1
    coordinates.append([x,i])

# Determine the number of rows we're ultimately going to have
x_vals = []
for point in coordinates:
    x_vals.append(point[0])
x_min = min(x_vals)
x_max = max(x_vals)
number_of_rows = (x_max - x_min) + 1

# set up the 'grid'
grid = []
for i in range(number_of_rows):
    grid.append('.')

# Put everything in positive terms by setting the lowest row number to 0
# and increasing all the row numbers by a relative amount
base_zero_mod = 0 - x_min
for point in coordinates:
    point[0] += base_zero_mod

# "draw" the image by updating each string in grid
z = 0
for y, x in coordinates:
    for i in range(len(grid)):
        if i == y and z == x: 
            grid[i] += seq[z]
        else:
            grid[i] += '.'
    z += 1

# Everything is constructed top down, do reverse it for printing purposes
grid.reverse()
for row in grid:
    print(row[1:])


  













