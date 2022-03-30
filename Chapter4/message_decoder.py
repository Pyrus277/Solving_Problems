#coci08c3p2
#
# Luka is fooling around in chemistry class again! Instead of balancing equations
# he is writing coded sentences on a piece of paper. Luka modifies every word in a
# sentence by adding, after each vowel (letters a, e, i, o and u), the letter p
# and then that same vowel again.
#
# Write a program that decodes the sentence.
#
# Input will be a single line string of only lowercase letters
# Output should be the decoded sentence on a single line.


string = input()
decoded = ''
x = 0
for letter in string:
    if x == 0:
        decoded += letter
        if letter in 'aeiou':
            x = 2
    else:
        x -= 1
print(decoded)

#(0.15s, 9.3M)
