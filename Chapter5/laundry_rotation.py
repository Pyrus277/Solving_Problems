# ecoo19r1p1

# Ian only does laundry when all shirts are dirty
# N - number of clean shirts to *start*

# If at the beginning of a day Ian only has dirty shirts,
# he will do laundry and make all owned shirts clean

# If he goes to an event, he will get one clean shirt

# Given N and the schedule of evens for the next D days, 
# how many times will Ian do laundry for the next D days?
 
# Input - 10 datasets
#   Line 1 - N, M (number of events), D 
#   Line 2 - M integers - days on which there are events

#Output - int times Ian will do laundry in the next D days


for i in range(10):
    # collect and make integers of our starting variables
    str_lst = input().split(' ')
    clean_shirts = int(str_lst[0])
    number_events = int(str_lst[1])
    days = int(str_lst[2])


    # collect and make an int list of the event schedule
    event_days = [int(x) for x in input().split(' ')]

    # initialize some more variables
    laundry_days = 0
    max_shirts = clean_shirts
    day_tracker = 1


    for day in range(days):
        # if he starts the day with no clean shirts, do laundry and make all owned shirts clean
        if clean_shirts == 0:
            laundry_days += 1
            clean_shirts = max_shirts
        # if it's an event day, increase the max number and clean number of shirts by one for
        # each event scheduled that day
        if day_tracker in event_days:
            max_shirts += event_days.count(day_tracker)
            clean_shirts += event_days.count(day_tracker)
        # increment clean shirts down, and day tracker up
        clean_shirts -= 1
        day_tracker += 1

    print(laundry_days)




