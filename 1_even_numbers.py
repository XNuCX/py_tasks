nums = input().split(" ")
print(list(filter(lambda x: int(x) % 2 == 0, map(int, nums))))