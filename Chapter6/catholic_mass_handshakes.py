# coci13c2p2

# Given a seating configuration for a Roman Catholic mass,
# return the number of handshakes made during the rite of peace.
# As part of this total number, consider how many handshakes will 
# occur if one straggler who arrives late takes a spot that will
# yield the greatest number of handshakes. 

# Inputs:
#   First line - two ints, representing the number of rows r and seats s
#   Next r lines - strings s characters long representing occupied 'o' and 
#   unoccupied '.' seats.
# Output: total number of handshakes. 


# The plan:

# 1. Get user inputs
# 2. Create the data structure:
#    2a. seats = [[],[]], with each sublist being a row(y), and each item being a seat(x),
#        and each seat being ON, OFF or E (empty). 

# 3. Iterate over each seat:
#    3a. If empty, count the number of adjacent occupied spots and keep track of the MaxPotential
#        (if MaxPotenial = 8 we can stop tracking this)

#    3b. If occupied, count the number of adjacent spots with the ON status and increment Handshakes.   
#        Each seat has an 8 part check.

# 4. Output Handshakes + MaxPotentialHandshakes
#    MaxPotentialHandhsakes will be 0 if every seat is occupied. 

# The algorithm:

# Get user inputs and build data structure:
rs = input().split(' ')
r = int(rs[0])
s = int(rs[1])
congregation = [] # the seating grid
# Appending in 'X' around the perimeter of the seating arrangement so when 
# we examine neighbors we never look at a spot that doesn't exist.
yBoundary = []
for i in range(s+2):
    yBoundary.append('X')
congregation.append(yBoundary)
for i in range(r):
    congregation.append(['X'] + list(input()) + ['X']) 
congregation.append(yBoundary)


def neighbor_count(x,y):
    ''' Takes the x & y coordinate of the subject point on a grid. We then look at all 8 grid points
    surrounding the subject point and return a list of what occupies those 8 spaces. The if statement
    in the list comprehension omits the subject point itself from consideration.
    '''
    neighbors = [congregation[col_mod + y][row_mod + x] for row_mod in (-1,0,1) for col_mod in (-1,0,1) 
                            if [row_mod + x, col_mod + y] != [x,y]]
    return neighbors

Handshakes = 0
MaxPotentialHandshakes = 0
for y, row in enumerate(congregation):
    for x, seat in enumerate(row):
        # For all the empty seats, we're gonna look at each neighbor. For each occupied space among the 
        # neighboring seats, we'll count to determine the total number of handshakes one would get if they
        # sat at the empty seat
        if seat == '.':
            neighbors = 0
            neighbors = neighbor_count(x,y)
            potentialHandshakes = neighbors.count('o') + neighbors.count('x')
            if potentialHandshakes > MaxPotentialHandshakes:
                MaxPotentialHandshakes = potentialHandshakes
        # For each occupied seat, we count how many handshakes that person would make, after which we
        # reset the value of the occupied space fom 'o' to 'x' so we don't recount a handshake with this
        # person when we examine their nighbors.
        if seat == 'o':
            neighbors = 0
            neighbors = neighbor_count(x,y)
            Handshakes += neighbors.count('o')
            congregation[y][x] = 'x'            

print(Handshakes + MaxPotentialHandshakes)

