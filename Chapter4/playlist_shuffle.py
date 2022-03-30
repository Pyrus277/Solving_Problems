#ccc08j2

#program a song playlist
# holds 5 songs in memory
# titles will always be 'A' 'B' 'C' 'D' 'E'
# keeps track of a playlist == the order of the songs
# 4 buttons that rearrange the playlist and play the songs:
#     1. Moves the first song to the end of the playlist
#     2. Moves the last song to the start
#     3. Swap the first two songs of the playlist
#     4. output the playlist
#
#Input:  program should repeatedly ask for two positive ints between b and n
#     b == button number, n == number of times to press that buttons
#   if b = 4, it can be assumed n = 1 and this will trigger the output of the playlist
#Output should be in the form "A B C D E"

p = 'ABCDE'
b = 0
n = 0
while b != 4:
    b = int(input())
    n = int(input())
    for i in range(n):
        if b == 1:
            p = p[1:] + p[0]
        if b == 2:
            p = p[4] + p[:4]
        if b == 3:
            p = p[1]+p[0]+p[2]+p[3]+p[4]

print(p[0],p[1],p[2],p[3],p[4])
