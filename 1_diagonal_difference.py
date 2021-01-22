size_of_matrix = int(input())
matrix = []
for _ in range(size_of_matrix):
    matrix.append([int(el) for el in input().split(" ")])
sum_main = 0
sum_secondary = 0
for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if row == col:
            sum_main += matrix[row][col]

for col in range(size_of_matrix):
    for row in range(size_of_matrix):
        if col == (len(matrix) - 1) - row:
            sum_secondary += matrix[row][col]
print(abs(sum_main - sum_secondary))

