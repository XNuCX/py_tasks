num = int(input())
names = []
even_set = set()
odd_set = set()
sums = 0
for i in range(1, num + 1):
    name = input()
    for char in name:
        sums += ord(char)
    sums = sums // i
    if sums % 2 == 0:
        even_set.add(sums)
    else:
        odd_set.add(sums)
    sums = 0

if sum(odd_set) == sum(even_set):
    print(', '.join([str(el) for el in (odd_set | even_set)]))
elif sum(odd_set) > sum(even_set):
    print(', '.join([str(el) for el in (odd_set - even_set)]))
elif sum(even_set) > sum(odd_set):
    print(', '.join([str(el) for el in (odd_set ^ even_set)]))