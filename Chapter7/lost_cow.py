# Problem can be found here: http://usaco.org/index.php?page=viewproblem2&cpid=735

# Use the algorithm that solves the "Lost Cow Problem" (see problem link)
# To see how far the farmer at position x would have to travel to find the
# cow at position y.

# My approach to solving this problem takes advantage of the predicable values
# assocated with each leg of the trip. You've got:
#   x_dist - The distance from the origin point which will, the abs val of which will be
#            increasing powers of 2, and the relative values of which will alternate between 
#            positive and negative.
#   leg_travel - The distance travled from the previous stopping point to the current x_dist.
#                In other words-- |previous x_dist| + |current x_dist].
#   total_travel - A running total, which accumulates the leg_travel distances.

# Input will be from a text file, the first number represending the farmer's position.
# and the second number the cows. 
# To simplify things I subtract the cow's poition from the farmer's and use this as the starting y
# position.


with open('./lost_cow_data/10.in', 'r') as fhand:
    inpt = fhand.read().split()
    farmer = int(inpt[0])
    cow = int(inpt[1])

# we're looking for when our x_dist originating from origin point 0 would coincide with y
y = cow - farmer


prev_x = None # Need to keep track of the previous leg's distance from x
# Inititalize the three variables mentioned above. These values represent 
# the completion of the first leg of the trip
x_dist = 1 
leg_travel = 1
total_travel = 1
  
exp = 1 # exponent value we'll be incrementing
indx = 1 # A value to keep track of the positive/negative value of x_dist

# We keep incrementing the three main values as long as y does not fall 
# within the x_distance.
while True:    
    if (abs(x_dist) >= abs(y)) and ((x_dist * y) > 0): #SIGNS MATCH
        break
    
    # Preserve the values of the previous leg.
    # We'll need these in conjunction with the final potentially "incomplete"
    # final leg of travel to get the final travel total
    prev_x = x_dist
    prev_leg = leg_travel
    prev_total = total_travel
    
    # Increment x_dist and assign the appropriate sign
    x_dist = 2**exp
    exp +=1 
    if indx % 2 != 0:
        x_dist = x_dist * -1
    indx += 1

    # Update values for the current leg
    leg_travel = abs(prev_x) + abs(x_dist)
    total_travel += leg_travel
    
# Calculate total travel. For the leg_travel for the final leg of the trip
# we only go as far as the absolute vale of y, rather than the abs val of the
# usual power of 2 x_dist.
leg_travel = abs(prev_x) + abs(y)
total_travel = prev_total + leg_travel

# Aaand we're done. So simple. This was so easy and I got it right away.
# Took me like 5 min.  
print(total_travel)


