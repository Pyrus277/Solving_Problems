# ccc13s1

# Given a particular year (0 <= year <= 10,000) as input,
# output the next year that has all distinct digits.

year = int(input()) + 1
while len(set(str(year).split()[0])) != len(str(year)):
    year += 1
print(year)
