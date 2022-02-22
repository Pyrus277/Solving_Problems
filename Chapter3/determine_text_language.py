#DMOJ ccc11s1

#determine if a given input of text is French or English based on the relative counts
# if the letters S and T. If T appears more, it's probably English.

#input will be a number N indicating the amount of lines that will be inputted
#followed by N number of lines of text.
#Output should be whether the text is French or English

t_ct = 0
s_ct = 0

for X in range(int(input())):
    line = input()
    t_ct += line.lower().count('t')
    s_ct += line.lower().count('s')

if t_ct > s_ct: print('English')
else: print('French')
