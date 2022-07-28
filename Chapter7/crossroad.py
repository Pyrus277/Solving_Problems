# This problem is found here: http://usaco.org/index.php?page=viewproblem2&cpid=711

# The input is a text file, the first line being a number N representing the number
# of observations made, and the following N lines being the observations.
# Each observation consists of two numbers-- the first being the cow id, and the second
# being a 1 or 0 representing the side of the road the cow is observed to be on. 

# If we observe a cow to be on a side of the road it was previously not observed to be
# on, this is a confirmed crossing. 

# Output the number of confirmed crossings. 

# Gather data from the input file.
with open('./crossroad_data/10.in', 'r') as fhand:
    inpt = fhand.read().splitlines()
# Get rid of the N line and turn the rest into a list of lists
# Note - these don't need to be integers for the purpose of this
# program.I just got lazy and copied the code here from the last 
# problem.
inpt.pop(0)
for i in range(len(inpt)):
    inpt[i] = [int(x) for x in inpt[i].split()]

# The approach here is to initialize a dictionary and count variable
# and iterate thru the observation list (inpt).
# If we encounter a cow id not in the dictionary, we add that id (key) to it
# and also the initial side of the road it's observed to be on (value).
# If, however, the id is in the dictionary, we look to see if the current
# side observation is different from the current value for that id key, and if
# so, we increment the crossing count and change the value to that of the
# current observation. Otherwise, we just leave it alone and move on to the next
# observation: 
obs_dict = {}
crossings = 0
for obs in inpt:
    if obs[0] not in obs_dict: 
        obs_dict[obs[0]] = [obs[1]]
    else: 
        if obs[1] != obs_dict[obs[0]][0]:
            crossings += 1
            obs_dict[obs[0]][0] = obs[1]
print(crossings)