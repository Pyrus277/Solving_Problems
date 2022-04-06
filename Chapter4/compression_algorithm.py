#ccc19j3

# write a simple run-length encoding compression program
# for each line of input, for consecutive repeated characters,
# output the number of repetitions and that character.
# i.e. 'eee!!!!@xx' ==> '3 e 4 ! 1 @ 2 x'

# Input:
# N == number of lines that follow.
# Following lines contain b/w 1 & 80 chars inclusive, no spaces
#
# Output:
# N lines
# Line i will be the encoding of the line i+1 of the input
# Encoding of a line will be a sequence of pairs, separated by a space,
# where each pair is an integer followed by a space, followed by a character

N = int(input())
for I in range(N):
    line = input()
    comp_str = ''
    count = 1
    i = 0

    while i < len(line):
    # check if we're at the end of the string
        # if the last character is not equal to the preceeding one, count = 1 and add
        # this count and character to the string
        if i == (len(line) - 1) and line[i] != line[-2]:
            count = 1
            comp_str = comp_str + str(count) + ' ' + line[i] + ' '
            break
        # if the last character is equal to the preceeding one, then add the current
        # count and character to the string
        elif i == (len(line) - 1) and line[i] == line[-2]:
            comp_str = comp_str + str(count) + ' ' + line[i] + ' '
            break

    # otherwise, if we're not at the end:
        # if the next character is not equal to the current one, count = 1 and
        # add the current count and character to the string, and reset the count.
        if line[i+1] != line[i]:
            comp_str = comp_str + str(count) + ' ' + line[i] + ' '
            count = 1
        # if the next character is the same, increment the count
        elif line[i+1] == line[i]:
            count += 1
    #increment the iteration value for the current line.
        i += 1
    print(comp_str)
