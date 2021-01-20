command = input()
count = 0
collected = {}
resource = ""
quantity = 0
flag = False
while not command == "stop":
    count += 1
    if not count % 2 == 0:
        resource = command
    else:
        flag = True
        if resource in collected:
            collected[resource] += int(command)
        else:
            collected[resource] = int(command)

    command = input()
for key, value in collected.items():
    print(f"{key} -> {value}")