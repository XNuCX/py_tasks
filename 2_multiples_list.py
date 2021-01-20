
factor = int(input())
count = int(input())
l = []
i = 0
while not len(l) == count:
    i += 1
    if i % factor == 0:
        l.append(i)
print(l)