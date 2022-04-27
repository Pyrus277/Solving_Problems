# ecoo18r1p1

# Willow likes to play with every box Mandy brings home
# Willow plays with a box for T days before getting bored of it
# Once bored, never again

# Once a box is done being played with, Mandy can use it
# If Mandy brings home another box before Willow finishes with it, 
#   Willow will wait until she is bored with the previous box before moving
#   on to the new one

# Given Mandy's box shopping habits over the next N days, can you determine
# by how many days the project will be delayed due to Willow?

# 10 datasets
# Line 1- two ints, T & N 
# Next N lines- E or B (B indicating a box)


for i in range(10):
    inp = input().split()
    T, N = int(inp[0]), int(inp[1])
    backlog = 0 
    for n in range(N):
        shopping = input()
        if shopping == 'E' and backlog == 0: # case where we start with E
            continue
        if shopping == 'B':
            backlog += T
            backlog -= 1        
        if shopping == 'E' and backlog > 0:
            backlog -= 1

    print(backlog)