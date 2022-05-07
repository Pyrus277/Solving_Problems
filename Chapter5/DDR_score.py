# wac3p3
# Comments that follow are a summary, see https://dmoj.ca/problem/wac3p3 
# for the full description including contraints.

# The DDR machine is broken and unable to keep track of Wesley's score
# Help to keep track of his score.
# 4 different moves-- (U)p, (D)own, (L)eft (R)ight
# Songs consist of multiple beats, and he will match each beat with
# a single move. Each move is 1 point.
# Each song S is described by a sequence of characters consisting of 
# U D L R. 
# A combo is defined by a specific ordering of moved played consecutively.
# There are M different combos, each associated with a different point
# value P, which is earned each time a combo is completed. 

# To determine which moves are part of combos, the following algorith is used:
# 1. Current move is the first move Wesley performs
# 2. From the defined combos, select the one with the longest sequence
#    starting from the current move. 
# 3. The current move then becomes the last move in the longest combo
#    or the move immediately after the current move if no combo exits
# 4. If the current move is past the end of the sequence, terminate,
#    otherwise, go to step t

# Inputs
# First line - string S-- UDLR etc..
# Second line - M - number of different combos
# Next M lines will contain C-- the combo sequence, and P-- the 
# points the combo is worth. 

# Output
# A single integer representing wesley's score. 

###################################
###################################

# collect inputs:
# make a list of moves
sequence = input()
# make a list of the combo lists
#   Each list will have a string representing the combo's sequence of moves, 
#   and an integer representing the corresponding score. 
combos = []
N = int(input())
for i in range(N):
    moves = input().split(' ')
    moves[-1] = int(moves[-1])
    combos.append(moves)

# basic score
score = len(sequence)

# combo scoring
matches = [] # This list holds all the possible combos that could follow from the current step i
in_combo = 0 # This varaible is to determine if the current step i should be skipped over if it
             # is part of a previously triggered combo, and thus be skipped for combo determination
for i in range(len(sequence)):
    if in_combo == 0: #only evaluate if the current step is not IN a previously started combo
        # create a list of possilbe combos the current step can kick off
        for combo in combos:
            if sequence[i:i + len(combo[0])] == combo[0]:
                matches.append(combo)
        # inialize
        combo_score = 0 # should correspond to the longest combo from matches
        max_len = 0
        # determine the longest combo (string length), and pull out the correxponding score to add to the overall score
        for match in matches:
            if len(match[0]) > max_len:
                max_len = len(match[0])
                combo_score = match[1]
        score += combo_score
        # we just scored a combo, so we should "skip" the next number of values in sequence equal to the length
        # of the combo just scored including the current i 
        in_combo = max_len
    # decrement the remaining number of moves we're skipping
    if in_combo != 0:
        in_combo -= 1
    matches = []

print(score)



