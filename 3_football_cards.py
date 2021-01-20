cards = input()
text = ""
count_a = 0
count_b = 0
player_a = ""
player_b = ""
for char in cards:
    if char == " " or char == "-":
        continue
    text += char
text = list(text)
for i in range(0, len(text)):
    a = i
    if text[i] == "A":
        if not a+4 > len(text):
            if text[i+1] == player_a or player_a == str(text[i+1]+text[i+2]):
                continue
        player_a = text[i+1]
        if not a + 4 > len(text):
            if 48 <= ord(text[i+2]) <= 57:
                player_a += text[i+2]

        if count_a == 5:
            break
        count_a += 1

    if text[i] == "B":
        if not a + 4 > len(text):
            if text[i+1] == player_b or player_b == str(text[i+1]+text[i+2]):
                continue
        player_b = text[i + 1]
        if not a + 4 > len(text):
            if 48 <= ord(text[i+2]) <= 57:
                player_b += text[i+2]
        if count_b == 5:
            break
        count_b += 1

print(f"Team A - {11-count_a}; Team B - {11-count_b}")
if count_a == 5 or count_b == 5:
    print("Game was terminated")