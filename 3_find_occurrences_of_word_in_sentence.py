import re
sentence = input()
word = input()
count = 0
pattern = fr"\b{word}\b"
matches = re.finditer(pattern, sentence, re.IGNORECASE)
for match in matches:
    count += 1
print(count)

