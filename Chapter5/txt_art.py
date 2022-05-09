# coci19c5p1

# 1. turn the inputs into lists
# 2. Start iterating until we hit a *
# 3. Determine the area of the rectangle.
# 4. Resume iteration, but only in spots
#    outside of and one space away from the area
#    of the rectangle that we determined. 
# 5. When another * is hit, go back to 3.

x = input().split(' ')
lines = int(x[0])
chars = int(x[1])

grid = []
first_row = []
rectangles = 0

for i in range(chars+1):
    first_row.append('.')
grid.append(first_row)

for line in range(lines):
    row = ['.']
    for char in input():
        row.append(char)
    grid.append(row) 

y = 0
for r in grid:
    x = 0
    for c in r:
        if c == '*' and grid[(y-1)][x] == '.' and grid[y][(x-1)] == '.':
            rectangles += 1    
        x += 1
    y += 1

print(rectangles)    
    





