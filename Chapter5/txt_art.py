# coci19c5p1

# Daniel is making some text art in a text editor.
# The pictures will consist of even rows of '.' and '*'.
# The * characters will form non-overlapping rectanles.
# The rectangles will also not touch each other on any of 
# their surfaes. 
# Write a program to count the number of rectangles Daniel drew.

# Input:
# First line: N number of rows, M number of characters per row.
# Following lines - the sequences of . and *

# Output: 
# The number of rectangles drawn

# My approach:
# Given the contraints of the rectangles, each one will necessarily
# have an upper left corner that is not directly adjecent to another
# * charater to the immediate left and above.
# Scan each character to see if it's a '*' and if it meets that 
# that criteria, and if so, increment the rectangle count.
# (I added in a row and column of only . characters to make this easier).


# collect inputs for the number of rows and columns
x = input().split(' ')
lines = int(x[0])
chars = int(x[1])

grid = []
first_row = []
rectangles = 0

# create the blank top row, and begin the list of lists which 
# make up the image grid
for i in range(chars+1):
    first_row.append('.')
grid.append(first_row)

# collect inputs for the character sequences preceding each with a '.' to 
# make a blank column. Then append each of these rows to the grid
for line in range(lines):
    row = ['.']
    for char in input():
        row.append(char)
    grid.append(row) 

# iterate thru the cells and test for * characters with a . directly above and to the left   
y = 0
for r in grid:
    x = 0
    for c in r:
        if c == '*' and grid[(y-1)][x] == '.' and grid[y][(x-1)] == '.':
            rectangles += 1    
        x += 1
    y += 1

print(rectangles)    
    





