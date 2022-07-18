# This one was no joke.
# Problem can be found here:
# http://usaco.org/index.php?page=viewproblem2&cpid=920

# A drought has left Farmer John's N pastures devoid of grass, 
# but the rainy season is coming.
#
# In the shed are 4 buckets, each with a different type of
# grass seed. He wishes to sow each pasture with one of these
# types of seeds. He also wants to make sure each of his cows
# has a varied diet.
#
# Each of his M cows has 2 favorite pastures, and he wants to 
# be sure different types of grass are planted in each, so each
# cow can choose between two types of grass. 
# Also, no pasture is a favorite of more than 3 cows.
#
# Help Farmer John choose a grass type for each pasture so the
# nutritional needs of all the cows are met. 

# To summarize: 
# N pastures, each with 1 type of grass, each the favorite of no more than 3 cows
# M cows, each with 2 favorite pastues, each requiring 2 types of grass
# 4 grass types

# Input -- Read from a file
#    First line: Number pastures: N (2 <= N <= 100), number cows: M (1<= M <= 150)
#    Next M lines: Two ints - favorite pastures for each cow.
# Output -- Write to a file
#   N digit number, each digit 1..4, describing the grass type for each field.
#   First digit corresponds to pasture one, second to pasture 2 and so on. 
#   If there are multiple solutions, print the smallest N digit number amongst them. 

# Approach:
# Build a data structure like [[grass type, [cows]], [grass type, [cows]]...]
#                                  ^ i == field number
# Start with the lowest possible output number: For 5 fields-- 111111
# Increment until you find the soln

# Read the file and store the data
with open('./farm_seeding_data/1.in', 'r') as fhand:
    inpt = fhand.read().splitlines()
for i in range(len(inpt)):
    inpt[i] = [int(x) for x in inpt[i].split()]

number_of_pastures = inpt[0][0] 
number_of_cows = inpt[0][1]     

# create and populate your farm data structure
# farm = [ [ grass type int, [cow, cow...] ], [ grass type int, [cow, cow...] ]...  ]
farm = ['Fields:']  # made index 0 a dummy string so index 1 == field 1, but this turned out to not be necessary
for i in range(number_of_pastures + 1):
    if i == 0: continue
    if i >= 1:
        farm.append([1, set()])
   #cow
for i in range(len(inpt)):
    if i == 0: continue
    for num in inpt[i]:
        farm[num][1].add(i)

# If two fields share a cow (field1.isdisjoint(field2) == False) and grass type between
# them is the same, increment or decrement so the field later in the farm list has a 
# grass value of one higher. Targeting the later field for this so we find the solution
# that results in the lowest output number.

# You gotta keep the loop going until you go from the beginning to the 
# end without hitting a case that needs adjustment.
# For reference:
#    farm[][0] == grass type
#    farm[][1] == cows on field

check_again = 1
while check_again != 0:
    # Check all the fields by all the other fields
    check_again = 0 # If this remains zero, i.e. we don't hit a case that breaks a rule, we wont loop again.
    for x in range(1,len(farm)):
        for y in range(1,len(farm)):
            if x == y: continue # So we don't compare a field with itself.
            # If farm[x][1] and farm[y][1] share any cows and they have different grasses, great, do nothing
            if farm[x][1].isdisjoint(farm[y][1]) == False and farm[x][0] != farm[y][0]:
                continue
            # If farm[x][1] and farm[y][1] share any cows and they have THE SAME grass, change the grass
            # type of the field later in the sequence. This is the key bit of logic right here.
            if farm[x][1].isdisjoint(farm[y][1]) == False and farm[x][0] == farm[y][0]:
                check_again = 1
                if x < y:
                    farm[y][0] += 1
                elif y < x:
                    farm[x][0] += 1
# Finally we build our output and write it to a file
output = ""
for i in range(1,len(farm)):
    output += str(farm[i][0])
with open("out.out", "w") as file1:
    file1.write(output)



