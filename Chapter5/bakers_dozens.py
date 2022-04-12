# ecoo17r3p1

# -Input, 10 datasets that are like:
# First line -- There are F franchises, and D days of records
# This will be followed by D lines, each with F items (units sold), for each franchise.
#
# -Output
# 1. for each day, how many exact multiples of 13 were sold?
# 2. for each franchise across all days, how many exact multiples of 13 were sold?
#
# Output the total!

# Hard coded test variables
# F = 4
# D = 5
# DS = [ [4,3,2,4], [3,3,2,1], [8,2,4,1], [2,2,4,3], [9,3,2,3] ]

# for 10 datasets
for i in range(10):
    # get user inputs
    F_D = input()
    F, D = int(F_D[0]), int(F_D[2])
    # Make a list of lists
    DS = []
    for j in range(D):
        day = input().split()
        for k in range(F):
            day[k] = int(day[k])
        DS.append(day)

    bakers_dozens = 0

    # Sum the daily totals (row)
    for day in DS:
        if sum(day) % 13 == 0:
            bakers_dozens += sum(day)/13

    # Sum the totals by franchise (columns)
    for f in range(F):
        fsum = 0
        for d in range(D):
            fsum += DS[d][f]
        if fsum % 13 == 0:
            bakers_dozens += fsum/13

    print(int(bakers_dozens))
