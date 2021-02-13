size = int(input())
number_of_bombs = int(input())
bombs_with_positions = {}
field = []

for r in range(size):
    row = []
    for c in range(size):
        row.append(0)
    field.append(row)

for i in range(number_of_bombs):
    # bombs_with_positions.update({i: eval(input())})
    x, y = eval(input())
    field[x][y] = "*"

def action(r1, c1):
    def check_valid_idx(i, k):
        if i in range(size) and k in range(size) \
                and field[i][k] != "*":
            return True
        else:
            return False
    def up(r, c):
        r = r-1
        return [r, c]

    def down(r, c):
        r = r+1
        return [r, c]

    def right(r, c):
        c = c+1
        return [r, c]
    def left(r, c):
        c = c-1
        return [r, c]
    def u_r(r, c):
        r2, c = up(r, c)
        r, c2 = right(r, c)
        return [r2, c2]
    def u_l(r, c):
        r2, c = up(r, c)
        r, c2 = left(r, c)
        return [r2, c2]
    def d_r(r, c):
        r2, c = down(r, c)
        r, c2 = right(r, c)
        return [r2, c2]
    def d_l(r, c):
        r2, c = down(r, c)
        r, c2 = left(r, c)
        return [r2, c2]

    func_list = [up, down, right, left, u_r, u_l, d_r, d_l]

    for func in func_list:
        n = 0
        if field[r1][c1] == "*":
            n = 1
        r4, c4 = func(r1, c1)
        if check_valid_idx(r4, c4):
            field[r4][c4] += n

for r1 in range(size):
    for c1 in range(size):
        action(r1, c1)

for r3 in range(size):
    print(" ".join([str(el) for el in field[r3]]))