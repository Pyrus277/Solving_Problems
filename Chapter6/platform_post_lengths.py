# crci07p1
# A series of platforms is set up for a platforming video game. 
# All the platform locations are set and each have a post coming down 
# from each end, half a unit in from that endpoint. 
# If a platform has another one beneath it that would intersect with 
# one of its posts, the post base would rest on that platform and not 
# the ground. Calculate the total length of all the posts.
# 
# Input: first line - The number of platforms n.
#        Following n lines: three numbers for each platform representing the
#        height y off the ground, the starting point x1 and the end point x2
#
# Output: Sum total of post length.


# Collect user inputs
n = int(input())
platforms = []
for i in range(n):
    platforms.append([input()])
# Break up the strings
for i, platform in enumerate(platforms):
    platforms[i] = platforms[i][0].split(' ')
# Set them up as ints
for platform in platforms:
    for i in range(len(platform)):
        platform[i] = int(platform[i])
# Order the list by the 2nd item, the x1 coodinate
platforms.sort(key=lambda x: x[1])

# Calculate post lengths: 
postlength = 0 
postbase = 0
for i, platform in enumerate(platforms):
    # Compare platform to all the others
    # Check to see if there is any relevant x range overlap, and if so, adjust the postbase
    for compare_platform in platforms:
        if platform[1] in range(compare_platform[1],compare_platform[2]):
            if compare_platform[0] < platform[0] and compare_platform[0] > postbase:
                postbase = compare_platform[0]
    postlength += platform[0] - postbase
    postbase = 0
  # Compare the current platform's x2 value to all the platforms looking for x range overlap
    for compare_platform in platforms:
        if platform[2] in range(compare_platform[1]+1,compare_platform[2]+1):
            if compare_platform[0] < platform[0] and compare_platform[0] > postbase:
                postbase = compare_platform[0]
    postlength += platform[0] - postbase
    postbase = 0
print(postlength)

# Regarding the x-range overlap comparisons-- because the post begins half a unit from an endpoint,
# If a platform beginning (x1) and platform ending (x2) overlap, we ignore this-- the posts will be
# staggered. If, however, two beginnings or two endings overlap--x1 and x1, or x2 and x2, we do
# adjust the postbase for these cases. This is accounted for in the range statements above.