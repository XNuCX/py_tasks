numbers = input().split(" ")
result = []
for _ in range(len(numbers)):
    result.append(numbers.pop())
print(' '.join(result))