# This problem can be found here: http://www.usaco.org/index.php?page=viewproblem2&cpid=736

# Input Files:
# First line contains two numbers - the count of each type of cow N, and the number 
#     of characters per line M for the followng 2N lines.
# The following N lines contain genome strings for spotted cows
# and the following N lines contain genome strings for plain cows
# These strings contain some sequence of the characters  A G C T

# We are looking for the number of positions that could account for
# spottedness. i.e. which position(s) on the sequence for spotted cows
# contains bases that do not occur in the same position for the plain 
# cows. 

for i in range(1,11):
    # Data structure will be two lists of sets, which can then
    # be easily compared:
    spotted = []
    plain = []
    
    with open(f'./phenotype_data/{i}.in', 'r') as fhand:
        # first realine gathers the respective counts
        counts = fhand.readline()
        type_count = int(counts.split()[0])
        base_count = int(counts.split()[1])

        # Next readline populates the spotted list
        for base in fhand.readline().rstrip():
            spotted.append({base})
        # Next (type_count - 1) readlines add to the sets in the spotted list
        for i in range(type_count -1):
            for i, base in enumerate(fhand.readline().rstrip()):
                spotted[i].add(base)

        # The following block does the same as above, but for the plain cows
        for base in fhand.readline().rstrip():
            plain.append({base})
        for i in range(type_count -1):
            for i, base in enumerate(fhand.readline().rstrip()):
                plain[i].add(base)

    # We then compare the lists and check each position for exclusivity
    count = 0
    for i in range(base_count):
        if spotted[i].isdisjoint(plain[i]):
            count += 1
    print(count)
