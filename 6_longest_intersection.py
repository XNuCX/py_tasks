n_lines = int(input())
longest_intersection = []
take_the_biggest_small = []
take_the_smallest_big = []
count = 0
result = []
for _ in range(n_lines):
    first, second = tuple(input().split("-"))

    first_sect = [int(el) for el in first.split(",")]

    second_sect = [int(el) for el in second.split(",")]

    take_the_biggest_small= max(min(first_sect), min(second_sect))
    take_the_smallest_big = min(max(first_sect), max(second_sect))
    longest_intersection.append([take_the_biggest_small, take_the_smallest_big])


intersection = [abs(el[0] - el[1]) for i, el in enumerate(longest_intersection)]
longest = max(intersection)
for i in range(len(longest_intersection)):
    if abs(int(longest_intersection[i][0]) - int(longest_intersection[i][1])) == longest:
        index = i
longest = longest_intersection[index]

for i in range(longest[0], longest[1] + 1):
    result.append(i)
print(f"Longest intersection is {result} with length {len(result)}")

