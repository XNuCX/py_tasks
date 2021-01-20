text = input()
lis = []
for char in text:
    lis.append(chr(ord(char)+3))
print("".join(lis))
