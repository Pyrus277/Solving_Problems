# Project prompt can be found here: 
#   http://usaco.org/index.php?page=viewproblem2&cpid=855

# Input file gives us three lines representing three buckets.
# Each line has two numbers-- the maximum bucket capacity, and its current level
# Exactly 100 pours will be made-- from bucket 1 to bucket 2, from bucket 2 to
# bucket 3 and from bucket 3 to bucket 1, and so on.
# On each pour will go until the first bucket is empty, or the second one is full.
# Output the level of each bucket after all 100 pours are made.

# A function to determine how much liquid will be tranferred from bucket a to b, and 
# to update the respective amounts of each.
def milk_xfer(a,b): 
    '''
    This function takes two lists, and returns the
    lists with the updated amounts.
    '''            
    # determine the transfer amount. It will be the lower value between the
    # remaining content of a, or however much capacity is left in b
    xfer_amnt = min(a[1],b[0] - b[1])
    a[1] -= xfer_amnt
    b[1] += xfer_amnt

    return a,b


# Read from the file and set up the bucket variables
bucket_list = []
with open('./mixing_milk_data/10.in', 'r') as fhand:
    for line in fhand.readlines(): 
        bucket = line.rstrip().split()
        bucket_list += bucket       
b1 = [int(bucket_list[0]), int(bucket_list[1])]
b2 = [int(bucket_list[2]), int(bucket_list[3])]
b3 = [int(bucket_list[4]), int(bucket_list[5])]

# Carry out the pour actions untill we complete the 100th pour, updating the
# bucket variables as we go.
pour = 0
while True:
    
    after_pour = milk_xfer(b1,b2)
    b1 = after_pour[0]
    b2 = after_pour[1]
    pour += 1
    if pour == 100:
        break

    after_pour = milk_xfer(b2,b3)
    b2 = after_pour[0]
    b3 = after_pour[1]
    if pour == 100:
        break

    after_pour = milk_xfer(b3,b1)
    b3 = after_pour[0]
    b1 = after_pour[1]
    if pour == 100:
        break

# Output - write to a file named bucket.out
with open("bucket.out", "w") as file1:
    file1.write(f"{str(b1[1])}\n")
    file1.write(f"{str(b2[1])}\n")
    file1.write(f"{str(b3[1])}\n")