from collections import deque
rows, cols = [int(el) for el in input().split(' ')]
snake_string = input()
snake = deque()
for char in snake_string:
    snake.append(char)

matrix = []
for r in range(rows):
    matrix.append([])
    for c in range(cols):
        matrix[r].append(snake[0])
        snake.append(snake.popleft())

for i, r in enumerate(matrix):
    if i % 2 == 0:
        print("".join(r))
    else:
        print("".join(reversed(r)))


