# ccc99s1

# Write a program that'll keep score for a simple 2-player game
# played with a standard 52 card deck

# The deck is shuffled and placed face down on the table
# Player A turns over the top card and places it on a discard pile
# Then player B turns over the next top card and places it 
# on the pile. 
# A and B will alternate like this until the deck is exhuasted

# Scoring:
# If a player turns over an ACE, with at least 4 cards remaining,
# and none of the next 4 cards is a high card, that player scores
# 4 points.
# If a player turns over a KING with at least 3 cards remaining
# and none of the next 3 cards is a high card, that player scores 
# 3 points
# If a player turns over a QUEEN with at least 2 cards remaining
# and none of the next 2 cards is a high card, that player scores
# 2 points
# If a player turns over a JACK, with at least 1 card remaining,
# and the next card is not a high card, that player scores 
# 1 point. 

# Input:
#   52 lines, name of a card in the deck
# Output:
#   Whenever a player scores, print "Player X scores n point(s)"
#   where X = A or B, and n = 1,2,3 or 4
#   At the end of the game, print the total score for each player
#       Player A: n point(s).
#       Player B: m points(s).

# collect the inputs to make your deck of cards
deck = []
for i in range(52):
    deck.append(input())

# initialize some variables
remaining_deck = 52
i = 0
a_score = 0
b_score = 0
high_cards = {'ace','king','queen','jack'}
card_score = {'ace':4, 'king':3, 'queen':2, 'jack':1}

def scoring(num):
    """
    This function will take the point value of a high card and print the relevant scoring
    sentence. It will also return an int which will be the point value of the play 
    """
    if (remaining_deck >= num) and (high_cards.isdisjoint(set(deck[i+1:i+(num+1)]))):
        if i%2 == 0: 
            print(f"Player A scores {num} point(s).")
        else: 
            print(f"Player B scores {num} point(s).")
        return num
    else: 
        return 0

# start flipping cards
for card in deck:
    remaining_deck -= 1 # decrement for the cards left in the deck
  
    if card in high_cards:  
        x = scoring(card_score[card]) # print the score note
        # on even numbered rounds, A scores the value returned by the scoring. Odd numbered rounds, B scores.
        if i%2 == 0: a_score += x
        else: b_score += x
    #increment the index number.
    i += 1

print(f'Player A: {a_score} point(s).')
print(f'Player B: {b_score} point(s).')

