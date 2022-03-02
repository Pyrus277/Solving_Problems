# DMOJ coci13c3p1

#You see a screen with the letter A on it.
#You press the button and the A turns into a B
#You press it again and the B turns into BA
#further presses turns the BA into BAB and that into
#BABBA.

#input-- the number times K you press the button
#output-- the number of As and number of Bs in the
#resulting string.

#The mechanism:
# A --> B
# B --> BA


# #initialize
# next_sequence = ""
# #K = int(input())
# a_count = 0
# b_count = 0
# K = 4
#
# for n in range(K):
#     #initialize sequence for the starting state
#     if n == 0:
#         sequence = "A"
#     #make the string of the last run, the starting string of this one,
#     #and refresh the next_sequence veriable:
#     else:
#         sequence = next_sequence
#         next_sequence = ""
#     # go thru the string and produce the new output:
#     for letter in range(len(sequence)):
#         if sequence[letter] == "A":
#             next_sequence += "B"
#         if sequence[letter] == "B":
#             next_sequence += "BA"
#         print(next_sequence)
#
# #print(a_count,'',b_count)
# print("\nTotals:\nNumber of button presses:", K, "\nNumber of As:",next_sequence.count('A'),"\nNumber of Bs:",next_sequence.count('B'))

# The program above is all great if you want to track the actual sequences, but it quickly becomes compute heavy as K increases,
# and it failed the challenge for taking too long.
# It was a matter of just discovering the relationship between K, A, and B as K went up, and when you write out the numbers
#in columns for the first few iterations, the relationship becomes pretty clear, and is summarized in the passing solution below.


A = 1
B = 0
K = int(input())
for n in range(1,K+1):
    new_A = B
    new_B = A + B
    A = new_A
    B = new_B
print(A, B)
