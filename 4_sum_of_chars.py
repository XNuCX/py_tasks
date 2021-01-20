n = int(input())
result = 0
for i in range(1, n+1):
    char = ord(input())
    result += int(char)
print(f"The sum equals: {result}")
