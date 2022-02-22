#DMOJ coci18c3p1

#input takes a string
#go thru the string one letter at a time, and count how many times you can spell the word
#"HONI"


N = input()
honi_str = ''
honi_ct = 0
for letter in N:
    if letter == 'H' and 'H' not in honi_str: honi_str += 'H'
    if letter == 'O' and honi_str == "H": honi_str += 'O'
    if letter == 'N' and honi_str == "HO": honi_str += 'N'
    if letter == 'I' and honi_str == "HON": honi_str += 'I'

    if honi_str == 'HONI':
        honi_str = ''
        honi_ct += 1

print(honi_ct)
