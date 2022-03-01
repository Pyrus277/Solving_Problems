#DMOJ coci13c3p1

#given musical notes with no annotation, how to recognize scale used?
# use only A-minor and C-major

#A-min (A,B,C,D,E,F,G) main tones: tonic = A, subdominant = D, dominant = E
#C-maj (C,D,E,F,G,A,B) main tones: tonic = C, subdominant = F, dominant = G

#the main tones are the primary candidaates for accented tones in a composition,
#accented tones being the first tone of a measure. In the case of a tie, break
#it with the last tone, A for A-min, C for C-maj.

# write a program to decide id a composition is more likely A-min, or C-major
# by counting main tones


#inputs is one line between 5 and 100 chars from the set ABCDEFG|
#output 'C-dur' or 'A-mol'

import re
music = input()
#music = "CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C"

#gather all the accented tones
acc = list(music[0]) + re.findall('[|](.)', music)

#total the relative occurences of accented main tones:
amin = acc.count("A") + acc.count("D") + acc.count("E")
cmaj = acc.count("C") + acc.count("F") + acc.count("G")

#decide the output:
if amin > cmaj:
    print('A-mol')
elif amin < cmaj:
    print('C-dur')
elif music[-1] == 'C':
    print('C-dur')
elif music[-1] == 'A':
    print('A-mol')
