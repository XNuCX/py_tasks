n = 8
board = []
king_position = []
qeens_positions = {}
count = 0
for i in range(n):
    row = input().split(" ")
    if "K" in row:
        king_position.append(i)
        king_position.append(row.index("K"))
    if "Q" in row:
        for q in range(len(row)):
            if row[q] == "Q":
                qeens_positions.update({count: [i, q]})
                count += 1
    board.append(row)

flag = False

def moving_the_queen(r1, c1):
    flag = False
    def moving_right(*args):
        r, c = args
        c += 1
        return [r, c]

    def moving_left(*args):
        r, c = args
        c -= 1
        return [r, c]

    def moving_up(*args):
        r, c = args
        r -= 1
        return [r, c]

    def moving_down(*args):
        r, c = args
        r += 1
        return [r, c]

    def moving_r_u(*args):
        r, c = args
        r, c = moving_right(r, c)
        r, c = moving_up(r, c)
        return [r, c]
    def moving_r_d(*args):
        r, c = args
        r, c = moving_right(r, c)
        r, c = moving_down(r, c)
        return [r, c]
    def moving_l_u(*args):
        r, c = args
        r, c = moving_left(r, c)
        r, c = moving_up(r, c)
        return [r, c]
    def moving_l_d(*args):
        r, c = args
        r, c = moving_left(r, c)
        r, c = moving_down(r, c)
        return [r, c]
    list_func = [moving_right, moving_left, moving_up, moving_down,\
                 moving_r_u, moving_r_d, moving_l_u, moving_l_d]
    for func in list_func:
        r = r1
        c = c1
        while r in range(len(board)) and c in range(len(board)):
            r, c = func(r, c)
            if r in range(len(board)) and c in range(len(board)):
                if board[r][c] == "Q":
                    break
                elif board[r][c] == "K":
                    print([r1, c1])
                    flag = True
    if not flag:
        return False
    else:
        return True

for value in qeens_positions.values():
    if not flag:
        flag = moving_the_queen(value[0], value[1])
    else:
        moving_the_queen(value[0], value[1])
if not flag:
    print("The king is safe!")