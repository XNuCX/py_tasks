import re
pattern = r"-|,|\.|!|\?"
with open("text.txt", "r") as file:
    [print(' '.join(reversed(re.sub(pattern, "@", el).split()))) for i, el in enumerate(file.readlines()) if i % 2 == 0]
