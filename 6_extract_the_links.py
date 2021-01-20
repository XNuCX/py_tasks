import re
line = input()
text = ""
pattern = r"w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"
while line:
    text += line + " "
    line = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(f"{match.group()}")
