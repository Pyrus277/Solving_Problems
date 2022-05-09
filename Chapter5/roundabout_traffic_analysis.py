# ecoo18r1p2

# A street planning consulting company is looking to help
# the city prepare for converting a lot of their medium-
# traffice one-lane intersections into roundabouts. 

# After generating a plan, the city wants to run a simulation
# to see where the possible bottlenecks of traffic could be

# The simulation runs by finding the roundabouts along a 
# route and figuring out which roundabout is smallest in
# diameter. The smallest roundabout would be the best
# possible location for congestion and creating a bottleneck
# of traffic which would make the traffic patterns worse
# than they are now. 

# There are N roundabout-filled routes from the starting
# point to the endpoint. The task is to analyze different
# routes that are available to find out which route (or 
# routes) could generate the most issues. 

# Input
# 10 datasets. 
# First line int N = number of routes
# The next N lines each contain a series of ints describing
# a route. The first int of each route is the ID of the
# route. The second int is the number of roundabouts along
# the route. R ints follow which describe the diameter of 
# each roundabout along the route. 

# Output
# For each dataset, output the min roundabout diameter along
# a route followed by a brace-enclosed sored list of route
# IDs for routes that can cause issues. 

###############

# for each dataset, take the inputs and make a list of lists
# keep min diamater in a varable and update as you go thru the 
# lists(routes). If a diameter is in a list, put it in the output

# you need to sweep thru all the routes once to actually find
# what the min is, then you need to go again to build the output

#or maybe make one big list per dataset and use min function
# to find the min in one swoop. But then how to pick out the routes
# with that min if they're not collected and broken out in some way?


for I in range(10):
    # collect inputs and make a list of lists
    routes = []
    N = int(input())
    for i in range(N):
        routes.append([int(x) for x in (input().split(' '))])
    
    # Iterate thru the segments of the route lists that describe the roundabout diameters
    # and find the minimum one and put it in a variable
    min_diameter = None
    for route in routes:
        if min_diameter == None or min(route[2:]) < min_diameter:
            min_diameter = min(route[2:])

    # Iterate thru the segements of the route lists that describe the roundabout diameters,
    # except this time, if that set contains the minimum value we discovered, put the route's
    # corresponding ID in the list bottlenecks.
    bottlenecks = []
    for route in routes:
        if min_diameter in route[2:]:
            bottlenecks.append(route[0])

    # construct the required output with the curly braces, except they're NOT sets!
    bottlenecks = sorted(bottlenecks)
    str_bott = ''
    for i in range(len(bottlenecks)):
        if i == 0:
            str_bott += str(bottlenecks[i])
        else: str_bott += f',{str(bottlenecks[i])}'

    print(f'{min_diameter} {{{str_bott}}}')



