# DMOJ coci06c5p1

#Three cups, follow the ball. Ball begins under cup x of cups x, y, z.
#Input is one string, a sequence of characters A B or C in some combination.
#up to 50 characters long.
#Each character in the string represents a movement of the cups:
# A swaps the first and second cup,
# B swaps the second and third,
# C swaps the first and third
# Output returns 1, 2 or 3, depending if the ball ends under cup x, y or z.

moves = input()
#initialize:
x = 1
y = 0
z = 0

for move in moves:
    if move == "A":
        if x == 1 : x = 0; y = 1
        elif y == 1: x = 1; y = 0
    if move == "B":
        if y == 1: y = 0; z = 1
        elif z == 1: y = 1; z = 0
    if move == "C":
        if x == 1: x = 0; z = 1
        elif z == 1: x = 1; z = 0

if x == 1: print(1)
if y == 1: print(2)
if z == 1: print(3)
