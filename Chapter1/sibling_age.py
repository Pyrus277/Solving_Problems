#DMOJ Code: ccc13j1

#inputs are the ages of the youngest sibling and the middle sibling
#output the age of the oldest sibling

Y = int(input())
M = int(input())

O = M + (M-Y)

print(O)
