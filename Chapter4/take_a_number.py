#ecoo13r1p1

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
