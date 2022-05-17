# dmopc19c5p2

# Video game where player must defeat bots
# Player and the enemy each start with H health.
# Then the two take turns performing actions with the 
# player going first. 
# On each turn one can perform one of two actions:
#   A d: Attack opponent, dealing d damage
#   D d: Dodge your opponent if they attack on the next turn.
#        If the opponent does not attack next turn, take d damage
#
# Charlie has hacked the game and created two lists of N actions
# each representing what the opponent will do and what he will do.
# Your job is to simulate his battle and find out who wins.
# Note: Dodging at the end of the list of actions counts as a 
# failed dodge. (i.e. if the enemey prepares a dodge as their last
# move, they will inflict sel-harm 
#
# If any person's health reaches 0 or below, your program is to 
# output the correct answer and terminate
#
# Input:
#   First line: N H (number of moves, and starting health)
#   Next N lines: A or D and an integer representing Charlie's
#                 actions.
#   Next N lines: Same as above, but for the opponent's actions.
# Output:
#   VICTORY if Charlie wins, DEFEAT if he loses, or TIE if neither die.

import itertools  # Library to help merge two lists
# Gather inputs -- number of actions for each player and starting health h
inpt = input().split() 
total_actions = int(inpt[0])
h = int(inpt[1])

# Divide up the player and bot move sets, put them into individual lists 
# and format the details of each move to be a sublist like: 
#   [(player or bot action),(Attack or Dodge), (Damage amount)]
player_actions = []
bot_actions = []
for i in range(total_actions*2):
    A = input().split() 
    if i < total_actions:
        player_actions.append(['player',A[0],int(A[1])])
    else:
        bot_actions.append(['bot',A[0],int(A[1])])
# Merge our two individual lists into one main list of actions where the player moves 
# and bot moves are alternated in the order of actual play
actions = list(itertools.chain.from_iterable(zip(player_actions,bot_actions)))

# set up some varaibles to determine the outcomes of various moves
player_hp = h
bot_hp = h
player_dodge = 0
bot_dodge = 0
dodge_fail_dmg = 0
# iterate thru the ordered actions list
for action in actions:
    # Player turn logic
    if action[0] == 'player': # if it's the player's turn
        if action[1] == 'A':  # ..and they choose to attack
            if bot_dodge == 0: # ..and the bot did not preemptively dodge,
                bot_hp -= action[2] # the bot takes damage
            player_dodge = 0 # either way, reset the player dodge state
            dodge_fail_dmg = 0 # ..and the failed dodge damage value
        if action[1] == 'D': # if the player chose to dodge
            if bot_dodge == 1: # ..and the bot had chosen to dodge on its last turn
                bot_hp -= dodge_fail_dmg # .. the bot takes damage
            player_dodge = 1 # ..either way, put the player in the dodge state
            dodge_fail_dmg = action[2] # ..and adjust the dodge fail damage value 
    # Bot turn logic (same as block above, just with the roles reverse)       
    if action[0] == 'bot':
        if action[1] == 'A': 
            if player_dodge == 0:
                player_hp -= action[2]
            bot_dodge = 0
            dodge_fail_dmg = 0
        if action[1] == 'D':
            if player_dodge == 1:
                player_hp -= dodge_fail_dmg
            bot_dodge = 1
            dodge_fail_dmg = action[2]
    # Break out of this loop should either side hit zero HP
    if player_hp <= 0 or bot_hp <= 0:
        break
# The case where if the bot player chooses the dodge at their last action
if actions[-1][1] == 'D':
    bot_hp -= actions[-1][2]

# Print outcome condition
if player_hp > 0 and bot_hp > 0:
    print('TIE')
elif player_hp <= 0:
    print('DEFEAT')
elif bot_hp <= 0:
    print('VICTORY')