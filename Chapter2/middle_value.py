# DMOJ ccc07j1

#find the middle value from three inputted values
#(all different integers 0<=100<=)
b1 = int(input())
b2 = int(input())
b3 = int(input())

bowls = sorted([b1, b2, b3])
print(bowls[1])
