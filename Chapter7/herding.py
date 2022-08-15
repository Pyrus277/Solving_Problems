# This problem can be found here: http://usaco.org/index.php?page=viewproblem2&cpid=915

# A farmer has a long, narrow farm which can be likened to a number line, and spread
# out along the farm are three cows.
# The farmer is looking to herd them-- get them to occupy adjacent positions.
# Rules - Only one of the outer two cows can be moved, and it must move to a position
# somewhere in between the other two.

# Determine the minimum number of total moves to get the cows to be adjacent to one another
# And determine the maximum amount of moves to get the cows adjacent. 

# Approach:
# Final move - If two cows have exactly one empty space between them, the other
# cow must move there.

# 1. If cows begin in consecutive spaces, min and max both 0

# 2. Most efficient - Move an outer cow to an inner spot once space away from
# one of the other two cows, then do the final move. This way..
#   if two of the cows begin exactly one space away from each other, then mix_moves = 1
#   if two cows begin adjacent to each other, then mix_moves = 2
#   if no pair of cows begin adjacent or exactly once space away from each other, mix_moves = 2

# 3. Least efficient - Move an outer cow to an inner spot adjacent to one of the
# other two cows. Repeat until final move. 
#   Max = number of spaces between the two cows farthest from each other (difference - 1). 

# Gather data from the 10 input files.
for n in range(1,11):
    with open(f'./herding_data/{n}.in','r') as fhand:
        # Format the input string for each case as a list of 3 ints:
        p = [int(x) for x in (fhand.readline().split(' '))]
        
        # evaluation:
        # Two of the cows begin adjacent-- 2 moves.
        if p[1] - p[0] == 1 or p[2]  - p[1] == 1:
            min_moves = 2
        # Two of the cows begin once space apart-- 1 move
        elif p[1] - p[0] == 2 or p[2]  - p[1] == 2:
            min_moves = 1
        # No pair of cows begin adjacent or one space apart -- 2 moves
        else:
            min_moves = 2

        # Find the max number of moves using the least efficient approach:
        if (p[1] - p[0]) > (p[2]  - p[1]):
            max_moves = (p[1] - p[0]) - 1
        elif (p[1] - p[0]) < (p[2]  - p[1]):
            max_moves = (p[2]  - p[1]) -1 

        # If all three positions are consecutive, ignore above and set min and max to 0
        if p[2] - p[0] == 2:
            min_moves = 0
            max_moves = 0
        
        print(f'Input {n}:')
        print(min_moves)
        print(max_moves,'\n')
