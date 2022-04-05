#ecoo15r1p1

# obessive consumption of smarties: 
# separate them into color groups and eat them in this order:
# orange, blue, green, yellow, pink, violet, brown, red
# Everything except red gets eaten by the handful-- max handful = 7
# Red gets eaten one at a time.

# it takes 13 seconds to eat a handful of non reds
# each red takes 16 seconds

# after a big box is sorted, how long will it take to eat all
# the smarties?

# input --> 10 test cases
#   a test case consists of N lines where each line holds a color of
#   a single smertie in lower case
#   the last line will read 'end of box'

# output --> single line for each test case (ten lines) indicating
#   how long it will take to eat the entire box

# orange, blue, green, yellow, pink, violet, brown, red

import math
for i in range(3):
    #sort:
    smarties = []
    while True:
        smartie = input()
        if smartie == 'end of box':
            break
        smarties.append(smartie)

    #gather times
    orange = (int(math.ceil((smarties.count('orange'))/7)))*13
    blue = (int(math.ceil((smarties.count('blue'))/7)))*13
    green = (int(math.ceil((smarties.count('green'))/7)))*13
    yellow = (int(math.ceil((smarties.count('yellow'))/7)))*13
    pink = (int(math.ceil((smarties.count('pink'))/7)))*13
    violet = (int(math.ceil((smarties.count('violet'))/7)))*13
    brown = (int(math.ceil((smarties.count('brown'))/7)))*13
    red = (smarties.count('red'))*16

    #add them up and print
    total = orange+blue+green+yellow+pink+violet+brown+red
    print(total)
