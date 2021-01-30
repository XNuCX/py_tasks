dimensions = int(input())
matrix = []
for row in range(dimensions):
    matrix.append([int(el) for el in input().split(" ")])

command = input()
while not command == "END":
    action, row, col, val = [el if i == 0 else int(el) for i, el in enumerate(command.split(" "))]
    if row not in range(dimensions) \
            or col not in range(dimensions):
        print("Invalid coordinates")
        command = input()
        continue
    if action == "Add":
        matrix[row][col] += val

    elif action == "Subtract":
        matrix[row][col] -= val
    command = input()
[print(*[el for el in row]) for row in matrix]