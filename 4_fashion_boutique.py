clothes = [int(el) for el in input().split(" ")]
capacity_of_rack = int(input())
rack = []
count = 1
while clothes:
    if sum(rack) + clothes[-1] <= capacity_of_rack:
        rack.append(clothes.pop())
    else:
        count += 1
        rack = []
print(count)
