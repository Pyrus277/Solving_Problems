# ccc00s2.py

# A series of streams runs down a mountain
# At the foot of the mountain, several streams emerge as rivers
# Compute how much water flows in each river

# At any given elevation there are m streams, labeled 1 to m from left to right
# As we proceed down the mountain, one of the many streams may split into a left and
#   right fork, increasing the total number of streams(m) by 1.
#   Or, they may rejoin, reducing the total number of streams(m) by 1.
# After a split or rejoining occurs, the streams are renumbered from left to right
# 1 <= m <= 100

# Input:
#   line 1: n = initial # of streams at some high altitude
#   line 2 to n+1 = the flow of each stream from left to right
#   line n+2 and onwards: going down the mountainside, split and rejoin locations are encountered
#     for each split there will be three lines:
#       a line containing 99 means a split
#       a line containing an int indicates the number of the stream that is split
#       a line containing an int to indicate the percentage of flow to the left fork
#     for each join there will be two lines:
#       a line containing 88 means a join
#       a line containing an int indicating the number of stream that is rejoined with the
#           stream to its right. The flow of both streams is combined
#   77 will come after the last join or split and will indicate the end of input

# Output:
# the number of streams that emerge at the foot of the mountain
# and what the flow is in each (total flow?)


# Gather the flows of the inital streams:
streams = []
n = int(input())
for i in range(n):
    streams.append(int(input()))
# adjust stream states for splits and joins:
flow = 0
while flow != 77: # end on input 77
    if flow == 99: # for streams splits
        splitstream = int(input()) - 1
        splitpercent = (int(input())/100)
        x = streams.pop(splitstream)
        streams.insert(splitstream, x * (1 - splitpercent)) # right fork
        streams.insert(splitstream, x * (splitpercent)) # left fork
    if flow == 88: # for steam joins
        joinstream = int(input()) - 1 
        y = streams.pop(joinstream)
        z = streams.pop(joinstream)
        streams.insert(joinstream, (y+z))
        
    flow = int(input())

output = ''
for i in range(len(streams)):
    output += str(int(round(streams[i],0))) + ' '
print(output)