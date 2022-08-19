# dmopc19c5p1

# You are given a set of N items and M assignments.
# Each assignment requires T items. 
# If your set of items contains matches for all the items
# for a given assignment, you pass. If not, fail.
# Return the number of passed assignments. 

# Input
# Line 1: N, M
# Next N lines - list of items
# Next M sets of lines 
#   Line 1 - number of items T
#   Next T lines - items

# Output: Number of passes.

# Approach:
# Put all the items you got into a set.
# Put all the assignment items in a set on each iteration.
# Compare the sets and increment counter when appropriate.

# Situations:
# 1. The sets are exactly equal -- Increment
#   {a,b,c} & {a,b,c}
# 2. Base set has more than necessary -- Increment
#   {a,b,c} & {a,c}
# 3. Base set lacks an item -- Do not increment
#   {a,b,c} & {a,c,d}

backpack = set()
inpt = input().split(' ')
count = 0
for item in range(int(inpt[0])):
    backpack.add(input())
# print("backpack:",backpack)
for assignment in range(int(inpt[1])):
    reqs = set()
    for i in range(int(input())):
        reqs.add(input())
        # print("reqs:",reqs)
    if len(reqs.difference(backpack)) == 0:
        count += 1
print(count)




