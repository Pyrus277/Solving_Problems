#DMOJ Code: P1_dmopc15c7p2
# count the words in a simple text input

words = input("")
print(words.count(' ') + 1)

# alternatively(slighly slower):
# words = input("")
#
# print(len(words.split(' ')))
