t = input()
text = []
for el in t:
    text.append(el)

n = int(input())
field = []
player_position_col = 0
player_position_row = 0
for i in range(n):
    v = input()
    row = []
    for el in v:
        row.append(el)
    field.append(row)
    if "P" in row:
        player_position_col = row.index("P")
        player_position_row = i
m = int(input())

def action(r, c):
    if field[r][c] == "-":
        field[r][c] = "P"
        return
    else:
        text.append(str(field[r][c]))
        field[r][c] = "P"
        return

    pass

for _ in range(m):
    command = input()
    if command == "up":
        if player_position_row - 1 in range(len(field)):
            field[player_position_row][player_position_col] = "-"
            player_position_row -= 1
            action(player_position_row, player_position_col)
        else:
            if text:
                text.pop()

    elif command == "down":
        if player_position_row + 1 in range(len(field)):
            field[player_position_row][player_position_col] = "-"
            player_position_row += 1
            action(player_position_row, player_position_col)
        else:
            if text:
                text.pop()
    elif command == "left":
        if player_position_col - 1 in range(len(field)):
            field[player_position_row][player_position_col] = "-"
            player_position_col -= 1
            action(player_position_row, player_position_col)
        else:
            if text:
                text.pop()
    elif command == "right":
        if player_position_col + 1 in range(len(field)):
            field[player_position_row][player_position_col] = "-"
            player_position_col += 1
            action(player_position_row, player_position_col)
        else:
            if text:
                text.pop()

print(''.join(text))
for r in range(n):
    print(''.join(field[r]))
