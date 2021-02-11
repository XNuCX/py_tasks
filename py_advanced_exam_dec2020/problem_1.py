from collections import deque
males = deque([int(el) for el in input().split()])
females = deque([int(el) for el in input().split()])
n = 0
matches = 0
def check():
    if not males or not females:
        return False
    return True
while males and females:

    if males[-1] <= 0 or females[0] <= 0:
        # n += 1
        if females[0] <= 0:
            females.popleft()
            continue
        if males[-1] <= 0:
            males.pop()
            continue
    if not check():
        break
    if females[0] % 25 == 0:
        # n += 1
        females.popleft()
        if females:
            females.popleft()
        continue
    elif males[-1] % 25 == 0:
        # n += 1
        males.pop()
        if males:
            males.pop()
        continue
    if not check():
        break
    if males[-1] == females[0]:
        # n += 1
        matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males.append(males.pop() - 2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(el) for el in reversed(males)])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print(f"Females left: none")

# from collections import deque
# males = deque([int(el) for el in input().split()])
# females = deque([int(el) for el in input().split()])
# n = 0
# matches = 0
# while males and females:
#     m = males[-1]
#     f = females[0]
#
#     if int(m) <= 0 or int(f) <= 0:
#         # n += 1
#         if f <= 0:
#             females.popleft()
#             continue
#         if m <= 0:
#             males.pop()
#             continue
#
#     if int(f) % 25 == 0:
#         # n += 1
#         females.popleft()
#         if females:
#             females.popleft()
#         continue
#     if int(m) % 25 == 0:
#         # n += 1
#         males.pop()
#         if males:
#             males.pop()
#         continue
#     elif m == f:
#         # n += 1
#         matches += 1
#         females.popleft()
#         males.pop()
#     else:
#         females.popleft()
#         males.append(males.pop() - 2)
#
# print(f"Matches: {matches}")
# if males:
#     print(f"Males left: {', '.join([str(el) for el in reversed(males)])}")
# else:
#     print(f"Males left: none")
# if females:
#     print(f"Females left: {', '.join([str(el) for el in females])}")
# else:
#     print(f"Females left: none")