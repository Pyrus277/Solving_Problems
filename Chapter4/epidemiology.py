#ccc20j2

# when a person has a disease, they infect exactly R others, but only the next day
# no person is infected more than once
# we want to determine when a total of more than P people have had the disease

# Input -- 3 lines:
# P (Threshold number of people with the disease)
# N (Number of people with the disease on day 0)
# R (Number of people that each infected person will transfer the disease to)

# Output:
# The number of the first day on which the total number of people who have had
# the disease is > P


P = int(input()) # Threshold
N = int(input())   # start of day infections number
R = int(input())   # reinfect rate

day = 0
total_infected = N

while total_infected <= P:
    N = N * R
    total_infected += N
    day += 1

print(day)
