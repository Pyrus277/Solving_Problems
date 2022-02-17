#dmopc16c1p0

#input numberic values representing pizza qualities
#output sentence about how satisfied a customer is with the pizza based
#on the given qualities.

W = int(input())
C = int(input())

if W == 3 and C >= 95:
    M = 'absolutely'
elif W == 1 and C <= 50:
    M = 'fairly'
else:
    M = 'very'

print("C.C. is {} satisfied with her pizza.".format(M))
