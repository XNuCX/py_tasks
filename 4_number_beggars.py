l = list(input())
num = int(input())
flag = False
text = ""
newlist = []
result = 0
resultlist = []
for i in range(0, len(l)):
    if l[i] == "," or l[i] == " ":
        flag = True
        continue
    else:
        if flag:
            newlist.append(text)
            text = ""
        text += l[i]
        flag = False
        if i == len(l) - 1:
            newlist.append(text)

for beg in range(0, num):
    if beg >= len(newlist):
        resultlist.append(0)

    for i in range(beg, len(newlist), num):
        result += int(newlist[i])
        if i + num >= len(newlist):
            resultlist.append(result)
            result = 0
print(resultlist)