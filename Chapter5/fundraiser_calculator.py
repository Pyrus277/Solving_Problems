#ecoo17r1p1

# student council is organizing a school brunch where 50% of the proceeds will go
# to the year-end trip. Brunch price depends on student year-- $12, $10, $7, and
# $5 for years 1 to 4 respectively.

# Input contains 10 trips, 3 lines of data per trip.
#   The first line of trip data is the cost of the trip
#   The second line contains the percentage distribution of students from years
#       1 to 4 respectively.
#   The third line contains the number of students attending the brunch

# Output does the student council need to raise more money for the year end
# trip beyond the proceeds from the brunch?
#   YES or NO

from math import floor

for i in range(10):
    trip_cost = int(input())
    student_dist = list(input().split())
    num_students = int(input())

    price_brackets = [12, 10, 7, 5]
    max_sd = max(student_dist)
    total_collected = 0
    rounded_num_students = 0

    # determine if the floor() rounding led to any leftover students
    for i in range(len(student_dist)):
        rounded_num_students += floor(float(student_dist[i]) * num_students)
    leftovers = num_students - rounded_num_students

    # find the total collected, and add leftover students, if any, to the student distribution bracket with
    # the greatest size
    for i in range(len(student_dist)):
        if float(student_dist[i]) == float(max_sd):
            total_collected += ((float(student_dist[i])*num_students) + leftovers) * price_brackets[i]
        else:
            total_collected += (float(student_dist[i])*num_students) * price_brackets[i]

    if (total_collected/2) < trip_cost:
        print('YES')
    else:
        print('NO')
