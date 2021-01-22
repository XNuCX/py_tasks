row, col = [int(el) for el in input().split(" ")]
matrix = []
count = 0
square = []
for r in range(row):
    matrix.append(input().split(" "))

for r in range(row-1):
    for c in range(col-1):
        if matrix[r][c] == matrix[r][c+1] \
                and matrix[r][c] == matrix[r+1][c+1] \
                and matrix[r][c] == matrix[r+1][c]:
            count += 1
print(count)