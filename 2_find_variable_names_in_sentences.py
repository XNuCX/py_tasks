import re
text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+($|(?=\s))"
match = re.finditer(pattern, text)
result = []

for res in match:
    result.append(res.group())
print(*result, sep=",")