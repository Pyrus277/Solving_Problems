# crci06p1

# "Every evening villagers in a small village gather around a big fire and sing songs."
# If the bard is present (Villager number 1), he will play exactly
# 1 new song and everyone present will learn it.
# If the bard is not present, everyone who is will share all of the 
# songs they know with everyone else, and everyone there that night
# will then know all the same songs.

# Return the ids of all the villagers that know all of the songs
# sung during the given period.

# Input: 
# -Line 1: Number of villagers N
# -Line 2: Number of evenings E
# -Next E lines: The first item is the number of villagers present that
#  evening, followed by the IDs of these villagers.

#  Output:
# All villager IDs that know all the songs, one int per line
# in ascending order.



# General approach:
# -Each villager will have a set() of songs they know.
# -We're also gonna track an overall playlist.
# -After completing these sets and list, we're gonna return the 
#  villager IDs of all villagers whose sets match the playlist.

N = int(input()) # Number of villagers
E = int(input()) # Number of evenings.
villagers = [set('x')] # A list of sets. Important: the index number of this list
                       # will correspond to the villager ID. The first set there
                       # is a placeholder since there's no 0 villager.
playlist = [] # Initialize playlist. This will be populated with consecutive ints for each song. 
evenings = [] # Will be a list of lists for us to iterate over each evening.
for i in range(E):
    evenings.append([int(x) for x in (input().split(' '))])

# Populate the villagers list with empty sets for each villager.
for villager in range(1,N+1):
    villagers.append(set())

for evening in evenings: # Now we'll go thru each evening-- [1:] are the villager ids

    # If the bard is present...
    if 1 in evening[1:]:
        # Update the playlist with the one song he sings:
        if len(playlist) == 0:
            playlist = [1]
        else:
            playlist.append(playlist[-1] + 1)
    # And for each villager present, add the current playlist number to villagers' sets.
        for villager in evening[1:]:
            villagers[villager].add(playlist[-1])    
        
    # If the bard is not present...
    # Then everyone who is present (evening[1:]), synchronize their respective sets
    else:
        evening_setlist = set() # initialize a blank set for the evening.
        # We then iterate thru the villagers present and update the evening setlist 
        # with all the songs from each villager's set
        for villager in evening[1:]:
            evening_setlist = evening_setlist.union(villagers[villager])
        # We have the complete evening setlist, now we have synchronize each present villager's
        # own set with that one.
        for villager in evening[1:]:
            villagers[villager].update(list(evening_setlist))
# Finally we compare the set of each villager with that of the complete playlist
# and when these match, we return that villager's id.
for i, villager in enumerate(villagers):
    if villager.intersection(set(playlist)) == set(playlist):
        print(i)
