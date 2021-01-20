text = input()
lis = []
for index, char in enumerate(text):
    if index == 0:
        lis.append(char)
        continue
    if char != text[index-1]:
        lis.append(char)
print("".join(lis))

