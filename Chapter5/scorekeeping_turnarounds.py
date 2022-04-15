# coci18c2p1

# KJ is observing the task input for a basketball game and wants to answer the following:

# 1. How many points have been scored in the first half of the game, if we
#    know an entire game last 4 x 12 min

# 2. How many turnarounds have happened during the match?
#    That is, how many times has a team come from a losing position to a leading one?

# Keep in mind:
# one point max per second
# we know how many points Team A and Team B have scores, and the exact second
#    when it happened.

# Input:
#    Line 1: pos int, A, number of points team A has scored
#    Following A lines - the seconds where A was scoring points
#    This is then followed by the same info for team B

# Output:
#    int - number of points scored in the first half
#    int - number of turnarounds

# Here's a plan, make a list of tuples, and keep track of the game progress
# by iterating thru each of them
#
# 1. Take the inputs, package them in tuples and package them in a list
# 2. Sort the list by tuples
# 3. As you iterate thru the tuples, keep a tally of the total score and current
#    time, and return the halftime score
# 4. also track the current point leader, if a tie occurrs, and if the previously
#    losing team is now ahead.

# Collect inputs:
n1 = int(input()) # (number of points team A made)
ds = [] # setting up the data structure-- a list of tuples
# record team A scores
for i in range(n1):
    ds.append((int(input()), "A"))
# record team B scores
n2 = int(input()) # (number of points team B made)
for i in range(n2):
    ds.append((int(input()),"B"))
ds.sort() # data structure is like [(score time, scoring team), (score time, scoring team)...]

#Initialize variables
points = 0
A_score = 0
B_score = 0
turnarounds = 0
tie_game = None
winning = None

for second, team in ds:
    # gather points till halftime
    if second <= 1440:
        points += 1

# note turnarounds:
    # increment team scores
    if team == 'A':
        A_score += 1
    if team == 'B':
        B_score += 1

    # if prior round was a tie, and the team to score this round is not the team
    # that was most recently winning, then increment turnaround, otherwise, remove
    # the tied game status.
    if tie_game == 'yes' and winning != team:
        turnarounds += 1
        tie_game = 'no'
    else:
        tie_game = 'no'

    # track the current leader
    if A_score > B_score:
        winning = 'A'
    if B_score > A_score:
        winning = 'B'

    # update the tied game status, if applicable
    if A_score == B_score:
        tie_game = 'yes'
        #not resetting winning, because we want to maintain who was winning before the tie

print(points)
print(turnarounds)
