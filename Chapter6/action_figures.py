# This problem can be found at https://acm.timus.ru/problem.aspx?space=1&num=2144

# Gotta finish cleaning the room by putting the boxes of action figures
# on the shelf. 
# There are n boxes, numbered 1 to n. 
# Box i contains k(i) action figures, each of its now size a(i)(j).
# The figures must be put in a non-decreasing order by size. 
# If doing so is impossible, then cleaning cannot be finished at all.
# There are quite a few boxes, so it might be impossible. 
# Help determine if cleaning cannot be finished, or if it's 
# possible and she has to arrange the boxes anyway. 

# Input:
#   line 1: n = amount of boxes with action figures
#   Next n lines: k(i) = amount of figures in the (i)th box
#   followed by k(i) ints a(i)(j), sizes of action figures in
#   order from left to right

# The plan.
# 1. Get them inputs and make list of lists
# 2. Use sorted(list) to sort them lists, it will only use the
#       first value in each sublist
# 3. Then iterate thru the list of lists and start making
#       a cool new list from that of just integers, if we hit
#       a value that happens to be LESS than the one preceeding
#       it, then it's IMPOSSIBLE. Otherwise, possible.
#       Get coding, you slut.

# Get the inputs and make them into a sorted list of lists (sorted by first value)
n = int(input())
boxes = []
for i in range(n):
    box = [int(x) for x in input().split(' ')]
    boxes.append(box[1:])
boxes = sorted(boxes)

# initialize some variables
cleaning = [0]
unclean = 0

# Iterate thru the boxes and the figures within the boxes, and
# append the size value of each into a new list.
# If a value is ever entered into this list that is less than
# the preceding value, the cleaning task is deemed impossible. 
for box in boxes:
    for figure in box:
        if figure < cleaning[-1]:
            unclean = 1
            break
        else: 
            cleaning.append(figure)

# Outputs
if unclean == 1:
    print("NO")
if unclean == 0:
    print('YES')

