# ccc02j2
#
# input - a word
# if the word appears to use the American spelling,
#     output should be the canadian spelling
# if the word does not appear to use American spelling, it should
#     output without change.
# when the user types quit!x terminate
#
# American spelling detecton:
#   The word has more than 4 letters
#   It has a suffix of a consonant followed by 'or'
#If it's american spelling replace 'or' with 'our'
#Otherwise, just echo the word


while True:
    word = input()
    if word == 'quit!':
        break
    if len(word) > 4 and word[-3] not in ['a','e','i','o','u','y'] and word[-2] == "o" and word[-1] == 'r':
        print(word[:-2]+'our')
    else:
        print(word)
