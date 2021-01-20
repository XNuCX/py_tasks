text = input()
for index, emoji in enumerate(text):
    if index+1 not in range(len(text)):
        exit()
    else:
        if emoji == ":":
            print(f"{emoji}{text[index+1]}")