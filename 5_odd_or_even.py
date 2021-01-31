def pr(comm, l):
    if comm == "Odd":
        return sum([el for el in num_list if not el % 2 == 0]) * len(l)
    if comm == "Even":
        return sum([el for el in num_list if el % 2 == 0]) * len(l)
comm = input()
num_list = [int(el) for el in input().split()]
print(pr(comm, num_list))