#DMOJ Code ccc19j1
#Program input is the number of different types of shots each team made
#Output prints the game's winner after calculating the total scores and make a comparison


#team apples
a = int(input())*3 #3 pt shots
b = int(input())*2   #2 pt shots
c = int(input())   #1 pt shots
a_score = a+b+c

#team bananas
d = int(input())*3 #3 pt shots
e = int(input())*2   #2 pt shots
f = int(input())   #1 pt shots
b_score = d+e+f

if a_score > b_score:
    print('A')
elif b_score > a_score:
    print('B')
else:
    print('T')
