row, col = [int(el) for el in input().split(' ')]
matrix = [[el for el in input().split(' ')] for _ in range(row)]

commands = input()
while not commands == "END":
    if len(commands.split(" ")) != 5:
        print("Invalid input!")
    else:
        swap, row1, col1, row2, col2, *rest = commands.split(" ")
        if swap != "swap" \
                or int(row1) >= row \
                or int(row2) >= row \
                or int(col1) >= col \
                or int(col2) >= col:
            print("Invalid input!")
        else:
            matrix[int(row1)][int(col1)], matrix[int(row2)][int(col2)] = matrix[int(row2)][int(col2)], matrix[int(row1)][int(col1)]
            for r in range(row):
                print(" ".join(matrix[r]))
    commands = input()