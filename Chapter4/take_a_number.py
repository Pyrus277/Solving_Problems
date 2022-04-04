#ecoo13r1p1
# see full promt at https://dmoj.ca/problem/ecoo13r1p1
# it's a long one.

# bascially we're tracking a system where people waiting take a ticket
# inputs are the actions of 1. a person taking a new ticket, 2. a person being
# to, 3. the desk closing, and 4. input to trigger the end of the program.
# Upon each desk closure, the program should return a tally of 1. the number
# of people who waited that day, 2. the number still waiting when the desk closed
# and 3. the next number in the ticket machine.  



late = 0
waiting = 0

next_number = int(input())

while True:
    action = input()

    if action == 'TAKE':
        if next_number == 999:
            next_number = 0
        next_number += 1
        late += 1
        waiting += 1

    if action == 'SERVE':
        waiting -= 1

    if action == 'CLOSE':
        if next_number == 999:
            next_number = 1
        print(late, waiting, next_number)
        waiting = 0
        late = 0

    if action == 'EOF':
        break
