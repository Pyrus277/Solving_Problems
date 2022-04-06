#ccc07j3

# Program to help decide to take the offer given in a version of the game
# 'Deal or No Deal'
#
# Starts with ten briefcases containing various set sums.
# A number of cases will be opened  and removed and the contestant
# chooses whether to accept a dollar amount offer, or select one
# of the remaining suitcases. Write a program to help decide--
# if the banker's offer is greater than the average value of the
# remaining cases, they should take the deal.

# Inputs:
# n = how many cases opened
# A list of ints 1 to 10 representing values that have been eliminated.
# The banker's offer

# Output: 'deal' or 'no deal'

# Set the briefcase amounts
amounts = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
# how many cases to be eliminted
removed = int(input())
# zero out those list items
for i in range(removed):
    amounts[int(input())-1] = 0
# compare the deal to the average remaining value
if int(input()) > (sum(amounts)/(len(amounts)-removed)):
    print('deal')
else:
    print('no deal')
