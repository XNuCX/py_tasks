input_lines = int(input())
unique_elements = []
for _ in range(input_lines):
    unique_elements.extend(input().split(" "))
print('\n'.join(set(unique_elements)))


