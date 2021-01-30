# print(" ".join([j for i in [x.split() for x in input().split("|")[::-1]] for j in i]))
print(' '.join([' '.join([x for x in el if x.isdigit()]) for el in reversed(input().split("|"))]))