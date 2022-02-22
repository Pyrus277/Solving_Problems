# DMOJ ccc18j2

#Three inputs = N is number to total parking spaces; a sting N characters long representing
#occupied and unoccupied spaces where '.' and 'C', respectively.
#Output should be the number of spots there were occupied on *both* days.

# My first instinct was to use zip() and make a list of tuples.
#This approach didn't require the use of the N input.
# occupied = 0
# N = input()
# day1 = list(input())
# day2 = list(input())
#
# tot_park = list(zip(day1,day2))
#
# for (p1, p2) in tot_park:
#     if p1 == "C" and p2 == "C":
#         occupied += 1
# print(occupied)

#Alternatively (this approach might be more effient):

occupied = 0
N = int(input())
day1 = list(input())
day2 = list(input())

for space in range(N):
    if day1[space] == "C" and day2[space] == "C":
        occupied += 1
print(occupied)
