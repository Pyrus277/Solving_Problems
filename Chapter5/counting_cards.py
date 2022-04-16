# coci17c1p1

# blackjack
# player draws cards while sum of hand < 21 or until player says "DOSTA (stop)"

# cards = 52-- 13 ranks x 4 suits
#    number card = face number (2-10)
#    jack = 10
#    queen = 10
#    king = 10
#    ace = 11

# Caesar has already drew N cards, sum of which <= 21. 
# Should he draw another card?
# X is difference of the sum to 21
# **Don't** draw a card if # of remaining cards whose value is >= X is greater than
#    or equal to the number of remaining cards in the deck whose value is <= X

# Input:
# 1. N = number of cards drawn so far
# 2+ the value of each of the cards Caesar drew

# Output:
# VUCI (draw) or DOSTA

# number of remaining cards in the deck whose value is greater than X:
#      len([y for y in deck if y > X])
# number of remaining cards in the deck whose value is less than or equal to X:
#      len([z for z in deck if z <= X])

deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

X = 0
hand_sum = 0

handsize = int(input())
for n in range(handsize):
    card = int(input())
    hand_sum += card
    deck.pop(deck.index(card))

X = 21 - hand_sum

if len([y for y in deck if y > X]) >= len([z for z in deck if z <= X]):
    print('DOSTA')
else:
    print('VUCI')