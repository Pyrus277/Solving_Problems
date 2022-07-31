# This problem can be found at http://usaco.org/index.php?page=viewproblem2&cpid=963

# Input includes rows of values where each row represents a ranking of ID numbers.
# We want to track the number of pairs that maintain the same relative ranking
# to one another across observations. i.e. does ranking X always come before ranking
# Y across all observations?

def get_pairs(lst):
    '''Takes a list, returns a list of tuples for all the unique
    pairs of values in the list were one value in the list comes before
    another value in the list.'''
    pairs = []
    for i, x in enumerate(lst):
        # Thank you, Python, for accomodating for this kind of thing and not
        # giving me an out of range error here. 
        for y in lst[(i+1):]:
            pairs.append((x,y))

    return pairs

# An outer loop to adjust the open() string so we can run thru all the
# test case files in one swoop. 
for i in range(1,11):

    # Gather and format the data from the input file. We're gonna make
    # a list of lists for all the observation lines
    with open(f'./gymnastics_data/{i}.in', 'r') as fhand:
        nk = fhand.readline()
        data = fhand.readlines()
    observations = []
    for obs in data:
        obs = obs.rstrip().split(' ')
        obs = [int(x) for x in obs]
        observations += [obs]

    # Then we're gonna take the first observation and gather all relative positions 
    # of the different id numbers in the form of tuples
    consistent_pairs = get_pairs(observations[0])

    # We'll make similar lists of tuples for all the other observations, and compare each
    # to the first. If one of these subsequent lists does not contain a tuple that is in
    # the first list, it means the relative positions between those two IDs loses consistency.
    # We'll replace that value with an 'NA' which in effect trims the consistent_pair list down.

    for x in observations[1:]:
        comparison_pairs = get_pairs(x)
        for i, y in enumerate(consistent_pairs):
            if y not in comparison_pairs:
                consistent_pairs[i] = 'NA'
    # We'll then remove all those 'NA' placeholders and count the length of that list
    # to get the required output. 
    consistent_pairs = [x for x in consistent_pairs if x != 'NA']
    print(len(consistent_pairs))


