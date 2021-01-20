text = list(input())
l = []
flag = False
count_char = 0
count_1 = 0
count = 0
count_2 = 0
new_list = ""
second_list = []
for char in text:
    count += 1
    if char == " ":
        second_list.append(new_list)
        new_list = ""
    else:
        new_list += char
        if count == len(text):
            second_list.append(new_list)


for char in second_list:
    a = int(char)
    a = a - (a) - (a)
    l.append(a)
print(l)

