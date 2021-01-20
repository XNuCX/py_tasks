def check(number, targets):
    if number == -1:
        return -1
    elif number <= targets:
        return number + targets


sequence = input().split(" ")
sequence = [int(el) for el in sequence]
reduced_targets = len(sequence)
shot_target = 0
while True:
    command = input()
    if command == "End":
        sequence = [str(el) for el in sequence]
        print(f"Shot targets: {shot_target} -> {' '.join(sequence)}")
        break
    command = int(command)
    if command < len(sequence):
        if not sequence[command] == -1:
            old = sequence[command]
            sequence[command] = -1
            shot_target += 1
            sequence = [el - old if old < el else check(el, old) for el in sequence]
            
