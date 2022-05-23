# ccc18j3

# You're driving on a long straight road along which are five cities.
# As you travel you record the distance between each pair of consecutive cities.
# You would like to calculate a distance table that indicates the distance b/w
# each pair of consecutive cities you have encountered.

# Input: 
# Line 1: Four positive ints < 1000, each representing dist b/w consec cities in order

# Output:
# Output should be 5 lines with the ith line containing distance from city i to 
# cities 1,2,3,4,5 in order separated by one space.

# collect user inputs
distances = [int(x) for x in (input().split(' '))]

# create a list of distances from the first city
map = []
for i in range(len(distances)+1):
    map.append(sum(distances[:i]))

def ints_to_strs(distances):
    '''
    Function takes a list of integers and outputs a space separated
    string of these numbers.
    '''
    output = ''
    for distance in distances:
        output += str(distance)+' '
    print(output)


def distance_table_lines(map, num):
    '''
    Construct the distance table by subtracting each distance from city 1 from each distance
    from city 1 and returning the absolute value 
    '''
    line = [map[num]]
    for i in map[1:]:
        line.append(abs(i-line[0]))
    ints_to_strs(line)


for i in range(len(map)):
    distance_table_lines(map, i)


