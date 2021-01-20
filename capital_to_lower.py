import pyperclip
text = input().lower()
result = ""
text_1 = ""
text_2 = ""
exercise_number = ""

for i in range(0, len(text)):
    if 48 <= ord(text[i]) <= 57:
        if i == 0 and text[i] == "0":
            continue
        exercise_number += text[i]
        continue
    if ord(text[i]) == 46:
        exercise_number += "_"
        continue

    if text[i] == " " or text[i] == chr(9):
        i += 1
        continue
    if not i == " ":
        for n in range(i, len(text)):
            text_1 += text[n]
            n += 1
    break

for i in range(len(text_1) - 1, 0 - 1, -1):
    if text_1[i] == " " or text_1[i] == chr(9):
        i -= 1
        continue
    if not i == " ":
        for n in range(0, i + 1):
            text_2 += text_1[n]
            n += 1
    break

for i in text_2:
    if i == " ":
        i = "_"
    result += str(i)
print(exercise_number + result)
pyperclip.copy(exercise_number + result)
f = open(f"{exercise_number + result}.py", "a")