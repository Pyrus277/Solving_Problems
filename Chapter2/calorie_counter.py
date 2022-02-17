DMOJ Code#ccc06j1
#Program input takes an order from a customer
#Outputs the total calorie count of their selection

#Menu categories- Key Value pairs menu items and calorie count
b = {1:461,2:431,3:420,4:0} #Burger category
s = {1:100,2:57,3:70,4:0} #Sides
d = {1:130,2:160,3:118,4:0} #Drinks
ds ={1:167,2:266,3:75,4:0} #Desserts

order1 = int(input())
order2 = int(input())
order3 = int(input())
order4 = int(input())

sum = b[order1]+s[order2]+d[order3]+ds[order4]
print("Your total Calorie count is {}.".format(sum))
