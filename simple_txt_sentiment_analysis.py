#DMOJ code: ccc15j2

#input is a string of text that may or may not include some combination
#of happy and sad emojis
#output is a simple sentiment analsis of the text after parsing it and
#counting the emojis used

x  = input()

h = x.count(':-)')
s = x.count(':-(')
if h + s == 0:
    print("none")
elif h == s:
    print("unsure")
elif h > s:
    print("happy")
else:
    print("sad")
