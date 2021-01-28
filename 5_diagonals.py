n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split(", "))

first_diagonal =[int(x) for x in [', '.join([el for i, el in enumerate(matrix[r]) if i == r]) for r in range(n)]]
second_diagonal =[int(x) for x in reversed([', '.join([el for i, el in enumerate(matrix[(len(matrix)-1) - r]) if i == r]) for r in range(n)])]
sum_1 = sum(first_diagonal)
sum_2 = sum(second_diagonal)
print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum_1}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum_2}")