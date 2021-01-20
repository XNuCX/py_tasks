number = int(input())
result = []

for_print = []
for _ in range(number):
    commands = input().split(" ")
    if commands[0] == "1":
        result.append(int(commands[1]))
    elif commands[0] == "2":
        if result:
            result.pop()
    elif commands[0] == "3":
        if result:
            print(max(result))
    elif commands[0] == "4":
        if result:
            print(min(result))
if result:
    for _ in range(len(result)):
        for_print.append(result.pop())

    print(", ".join([str(el) for el in for_print]))
