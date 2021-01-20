import re
text = input()
pattern = r"(^|(?<=\s))([a-z0-9]+[\._-]?)+(?=@)@(?<=@)([a-z0-9]+[-]?\.?)+(?<=\.)([a-z0-9]+[-]?)+"
matches = re.finditer(pattern, text, re.IGNORECASE)
for match in matches:
    print(match.group(0))