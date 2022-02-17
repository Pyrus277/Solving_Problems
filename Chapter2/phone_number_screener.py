#DMOJ Code: ccc18j1

#input is a phone number
#test the phone number for a certain criteria and determine if it's a telemarketer
#output is to ignore or answer the call

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a == 8 or a == 9) and
        (d == 8 or d == 9) and
        (b == c)):
    print("ignore")
else:
    print('answer')
