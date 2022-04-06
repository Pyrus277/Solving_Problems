#ccc18s1

# relative village positions are represented by integers on a number line
# The "neighborhood" of a village is bounded by the halfway points between
# its position and the villag to the right and to the left
# Find the smallest village neighborhood.

# input:
# N = number of villages, number of lines to follow
# following lines will each contain one integer
#   the integer being V, the position of the corresponding village

# output:
#    the smallest neighborhood size with one digit after the decimal

# 1. Sort the list
# 2. For each village that isn't the first and last, find the SIZE.
#     SIZE = ((village - left_village)/2) + ((right_village - village)/2)
# 3. return the smallest size to one decimal place

# construct the sorted list of village locations
N = int(input())
villages = []
for I in range(N):
    village = int(input())
    villages.append(village)
villages.sort()

# initialize the iterator variable and size list
i = 0
sizes = []

# calculate the village sizes
for i in range(1,len(villages)-1):
    size = ((villages[i] - villages[i-1])/2) + ((villages[i+1] - villages[i])/2)
    sizes.append(size)
    i += 1
print(round(min(sizes),1))
