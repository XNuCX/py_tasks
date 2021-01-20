def shoot(index, power, available_indexes):
    if index in range(available_indexes):
        sequence_of_targets[index] -= power
        if sequence_of_targets[index] <= 0:
            sequence_of_targets.pop(index)


def add(index, power, available_indexes):
    if index in range(available_indexes):
        if index in range(available_indexes-1):
            sequence_of_targets.insert(index, power)
        else:
            sequence_of_targets.insert(index, power)
    else:
        print(f"Invalid placement!")


def strike(index, power, available_indexes):
    count = 0
    flag = False
    if index in range(available_indexes):
        for i in range(index - power, (index + power) + 1):
            if i in range(available_indexes):
                count += 1
        if count == power + power + 1:
            for i in range(index - power, (index + power) + 1):
                sequence_of_targets[i] = "Remove"
        else:
            flag = True
            print(f"Strike missed!")
        for _ in sequence_of_targets:
            if flag:
                break
            sequence_of_targets.remove("Remove")
            if "Remove" not in sequence_of_targets:
                break
    else:
        print(f"Strike missed!")


sequence_of_targets = input().split(" ")
sequence_of_targets = [int(el) for el in sequence_of_targets]
while True:
    commands = input().split(" ")
    if commands[0] == "End":
        sequence_of_targets = [str(el) for el in sequence_of_targets]
        print(f"{'|'.join(sequence_of_targets)}")
        break
    if len(commands) == 3:
        if commands[0] == "Shoot":
            shoot(int(commands[1]), int(commands[2]), len(sequence_of_targets))

        elif commands[0] == "Add":
            add(int(commands[1]), int(commands[2]), len(sequence_of_targets))

        elif commands[0] == "Strike":
            strike(int(commands[1]), int(commands[2]), len(sequence_of_targets))


