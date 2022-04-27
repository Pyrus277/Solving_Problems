# dmopc14c7p2

# Someone is taking tidal water level readings with a device that returns readings
# on an absolute scale of integers between 1 and 10,000.
# They want to know the difference between the max highest reading and the min 
# lowest reading.
# Assume that once the minimum low level is recorded, all subsequent readings will
# be a strictly increasing sequence of numbers
# If this sequence is not strictly increasing, it can be assumed a recording error
# has happened.

# Inputs
# Line 1 - the amount of readings taken
# Line 2 - a space-separated string of numbers that represents the readings
# Outputs
# The difference between the max high and min low, or in the case of an error,
# 'unknown'

# Gather the inputs and make a list of integers
N = int(input())
readings = input()
readings = readings.split(' ')
ints = []
for i in readings:
    ints.append(int(i))

# Determine the high tide max and low tide min, and initialize a counter, and tide progression value
max_high = max(ints)
min_low = min(ints)
count = 0
tide_progression = None # once this value is assigned a number, it means we have hit the minimum low as we iterate
                        # thru the readings

for i in ints:
    count += 1
    # Represents the case where we hit the low tide AFTER the high tide in the sequence
    if count == N and tide_progression == None:
        print("unknown")
        break
    # We hit the min_low and can start tracking the following sequence
    if i == min_low:
        tide_progression = i
        continue
    # We are tracking the sequence but have encountered a number lower that the one preceding, an error
    if tide_progression != None and i <= tide_progression:
        print("unknown")
        break        
    # We hit the max number without issue and we can return the difference between the max and min
    if tide_progression != None and i == max_high:
        print(max_high-min_low)
        break
    # The current number is greater than the preceding one, and we can increment the progression
    if tide_progression != None and i > tide_progression:
        tide_progression = i
