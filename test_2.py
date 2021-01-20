numbers = input().split(" ")
numbers = [el.split() for el in numbers]
result = []
for i in numbers:
    numbers_2 = [int(el) for el in i]
    numbers_2 = sum(numbers_2)
    result.append(numbers_2)
