#DMOJ wc17c3j3

# password pw must be (8 =< pw =< 10) chars. Just numbers and letters,
# and contain 3 >= [a-z], 2 >= [A-Z], 1 >= [0-9]

#program input is a possible password
#output says if it's valid or invalid

import re
pw = input()
lc = 0
uc = 0
num = 0

for char in pw:
    #count lowercase
    if re.search('[a-z]', char):
        lc += 1
    #count uppercase
    if re.search('[A-Z]', char):
        uc += 1
    #count numbers
    if re.search('[0-9]', char):
        num +=1

if lc >= 3 and uc >= 2 and num >= 1 and len(pw) >= 8 and len(pw) <= 12:
    print('Valid')
else:
    print('Invalid')
