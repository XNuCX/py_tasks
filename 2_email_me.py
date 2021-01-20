import math
email = input()
char_before = 0
char_after = 0
flag = False
for index, char in enumerate(email):
    if char == "@":
        flag = True
        continue
    if flag:
        char_after += ord(char)
    else:
        char_before += ord(char)
result = math.floor(char_before - char_after)
if result >= 0:
    print("Call her!")
else:
    print(f"She is not the one.")