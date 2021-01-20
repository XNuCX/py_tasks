numbers = input().split(" ")
finish_line = len(numbers) // 2
numbers = [int(el) for el in numbers]
zero_indexes = []
for index, el in enumerate(numbers):
    if el == 0:
        zero_indexes.append(index)
if zero_indexes
time_first = sum(numbers[0:finish_line])
time_second = sum(numbers[-1:finish_line:-1])
print(time_second)