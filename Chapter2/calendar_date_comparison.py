#DMOJ Code: ccc15j1

#input is a specific calendar date in 2015
#output is a determination if the input date is before, after, or on
#the february 


import time
m = input()
d = input()

user_date = time.strptime(m+'/'+d+'/'+'2015', '%m/%d/%Y')
ccc_date = time.strptime('2/18/2015', '%m/%d/%Y')

if user_date < ccc_date:
    print('Before')
elif user_date == ccc_date:
    print("Special")
else:
    print("After")
