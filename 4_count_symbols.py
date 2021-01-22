text = [el for el in input()]
text = tuple(text)
result = {}
for char in text:
    result[char] = text.count(char)
result = {k: v for k, v in sorted(result.items(), key=lambda x: x[0])}
for k, v in result.items():
    print(f"{k}: {v} time/s")


