path = input()
ext = path.split(".")
name = ext[-2].split(chr(92))
print(f"File name: {name[-1]}")
print(f"File extension: {ext[-1]}")

