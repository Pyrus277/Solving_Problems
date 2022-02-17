#DMOJ code: wc15c2j1

#input is a number N
#output repeat the word "far" N times in a given string

N = int(input())
N = N - 1
far = 'far, ' * N
print("A long time ago in a galaxy "+far+"far away...")
