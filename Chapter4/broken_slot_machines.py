#DMOJ ccc00s1

#This problem involves some predictable slot machines. Each play is 1 quarter.
#Machine 1 will pay out 30 quarters every 35 pulls
#Machine 2 will pay out 60 quarters every 100 pulls
#Machine 3 will pay out 9 quarters every 10 pulls

#The inputs are how many quarters Martha has to start, and how many pulls each
#machine has had since last paying out.
#Output should be how many plays it takes for Martha to go broke.


quarters = int(input())
machine1 = int(input())
machine2 = int(input())
machine3 = int(input())
playcount = 0

#The while statement is followed by 3 block of code, one for each machine
#Each block decrements a quarter, increments the playcount, and tracks the
#   payout value of the machine, paying out accordingly.
while quarters > 0:

    quarters += -1
    playcount += 1
    machine1 += 1
    if machine1 == 35:
        quarters += 30
        machine1 = 0
    if quarters <= 0: continue

    quarters += -1
    playcount += 1
    machine2 += 1
    if machine2 == 100:
        quarters += 60
        machine2 = 0
    if quarters <= 0: continue

    quarters += -1
    playcount += 1
    machine3 += 1
    if machine3 == 10:
        quarters += 9
        machine3 = 0

print(f"Martha plays {playcount} times before going broke.")
