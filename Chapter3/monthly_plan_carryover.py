#DMOJ coci16c1p1

# X = megabytes per month
X = int(input())
# N = number of months Pero has spent megabytes
N = int(input())
# initialize leftover variable
L = 0

for month in range(N):
    P = int(input())
    L += (X - P)  #allowance per month less usage to accumulate in the leftover L variable

print(L + X)
