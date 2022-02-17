#DMOJ code: wc18c3j1

#input is a volume of paint, a number of bottlecaps, and the value of a
#painted bottlecap.
#output the sale price of painted bottlecaps and leftover paint

P = int(input())  #liters of paint
B = int(input())  #liters per bottlecap to make a badge
D = int(input())  #value of each badge
                  # leftover paint is $1 per litre

#(P//B)*D = integer number of badges that can be made * value/badge, D
#P%B = vvalue of leftover paint at 1 pokedollar/liter

print((P//B)*D + (P%B))
