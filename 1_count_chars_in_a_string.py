text = input()
occurrences = {}
for char in text:
    if char == " ":
        continue
    if char in occurrences:
        occurrences[char] += 1
    else:
        occurrences[char] = 1
for key, value in occurrences.items():
    print(f"{key} -> {value}")
