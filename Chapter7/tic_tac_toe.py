# This problem can be found here: http://usaco.org/index.php?page=viewproblem2&cpid=831

# We are running a game of tic-tac-toe
# There are 26 different players, each represented by a different
# letter of the alphabet.
# Each of the nine spaces on a board can hold the initial of one player
# and any assortment of players might play on a single board.

# Players can win solo or in teams of two, i.e. if any one player has 
# only their initials in a row, column, or diagonal, that player wins 
# Likewise if a row, column, or diagonal is limited to the initials of two 
# players, those two players win.

# Each board is fully populated with initials before the wins are evaluated.

# For each board, return the number of individual players who can claim victory,
# and also return the number of two-player teams that can claim victory.

# Input: 3 lines each populated by some combination of letters from A to Z
# Output: 2 lines -- disticnt number of individual winners, distinc number of 
#         winning pairs. 

# Problem-solving approach:
# Somehow we need to:
# 1. Read from the file and populate a data structure
# 2. Use the structure to evaluate the rows, columns, and diagonals.
# 3. Add qualifying individuals and teams to their respective sets
# 4. Return the length of the sets.

# a loop for each of the 10 input files
for n in range(1,11):
    # Our data structure will be a simple 9 character string
    ttt = ''
    with open(f'./tick_tack_toe_data/{n}.in','r') as fhand:
        for line in fhand.readlines():
            ttt += line.rstrip()

    # Initialize the sets we eventually need to return the lengths of
    solo_winners = set()
    team_winners = set()
    # There's only eight fields to evaluate, so we can just write them out
    rcd = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(6,4,2)]

    # Evaluate each of the eight fields:
    for i in rcd:
        # Plug each field into a set. A field with set lengths of 1 or 2
        # will indicate a solo winner or team winners
        a = set(ttt[i[0]]+ttt[i[1]]+ttt[i[2]])
        # A field with a set length of 1 indiates a solo winner whom we will add
        # to a set.
        if len(a) == 1:
            solo_winners.add(''.join(a))
        # A field with a set length of 2 indicates a team win. And this team will be
        # added to a different set. 
        # To ensure only distinct teams are counted, the two initals of the winning 
        # team will be sorted alphabetically in a list, concatenated into a two-char string,
        # and this string will be added to the set.
        if len(a) == 2:
            a = sorted(list(a))
            team_winners.add(a[0]+a[1])
    
    print(f'File num {n}')
    print(len(solo_winners))
    print(len(team_winners),'\n') 
    


