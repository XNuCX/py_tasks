names = input().split(", ")
flag = False
result = []
names = [el for el in names if 3 <= len(el) <= 16]
for name in names:
    flag = False
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            flag = True
            break
    if flag:
        continue
    result.append(name)
print("\n".join(result))