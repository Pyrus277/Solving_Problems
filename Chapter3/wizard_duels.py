#DMOJ coci18c4p1

#There are 26 wizards, one for each letter of the aphabet
#   Input 1 - The wizard that starts with the Elder Wand
#   Input 2 - The number of duels that will take place
#   Input 3 to N - The winner and loser of a duel-- two uppercase lessers separated by a space
#If current holder of the Elder Wand is defeated, the winner of that duel then controls the
#   Elder Wand
#   Output 1 - The wizard holding the Elder Wand when all the duels are done
#   Outbut 2 - The number of different Wizards that held the Elder Wand



current_wandholder = input()
wandholders = [current_wandholder]
duels = int(input())

for duel in range(duels):
    result = input() # ex "X Y"
    if result[0] == current_wandholder or result[2] == current_wandholder:
        current_wandholder = result[0]
        if result[0] not in wandholders:
            wandholders.append(result[0])

print(current_wandholder)
print(len(wandholders))
