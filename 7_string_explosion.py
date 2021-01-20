text = input()
text_list = []
flag = False
n = -1
new_text = ""
flag_end = False
for i in text:
    text_list.append(i)

while not text_list == []:
    if flag and text_list[0].isdigit():
        n += int(text_list[0])
        while n != -1 and text_list[0] != ">":
            text_list.pop(0)
            flag = False
            n -= 1
            if not text_list:
                flag_end = True
                break
    if flag_end:
        break
    new_text += text_list.pop(0)
    if new_text[-1] == ">":
        flag = True
        continue

print(new_text)