rows, cols = input().split(" ")
rows = int(rows)
cols = int(cols)
matrix = []
for _ in range(rows):
    temp = [int(el) for el in input().split(" ")]
    matrix.append(temp)

matrixes = []
new_matrix = []
count_row = 0
count_col = 0
n = 0


def new_mat(row, col):

    if row + 3 <= rows and col + 3 <= cols:
        count = -1
        for r in range(row, row + 3):
            new_matrix.append([])
            count += 1
            for c in range(col, col + 3):
                new_matrix[count].append(matrix[r][c])
        matrixes.append(new_matrix)
    else:
        return


for row in range(n, rows):
    for col in range(cols):
        new_mat(row, col)
        new_matrix = []

if matrixes:
    temp_result = 0
    results = {}
    for i, mat in enumerate(matrixes):
        for line in mat:
            temp_result += sum(line)
        results[i] = temp_result
        temp_result = 0
    results = {k: v for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True)}

    for k, v in results.items():
        print(f"Sum = {v}")
        for line in matrixes[k]:
            line = [str(el) for el in line]
            print(' '.join(line))
        break

