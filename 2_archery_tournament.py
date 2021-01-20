def shoot_left(index, length, points, field):
    new_index = (index - length) % len(field)
    points += 5
    field[new_index] -= 5
    if field[new_index] < 5:
        points += field[new_index]
        field[new_index] = 0
    return points, field


def shoot_right(index, length, points, field):

    points, field = shoot_left(index, length, points, field)

    return points, field


def reverse_custom(field):
    field = reversed(field)
    return field


def game_over():
    return f"{' - '.join([str(el) for el in targets_in_field])}\nIskren finished the archery tournament with" \
           f" {collected_points} points!"


targets_in_field = input().split("|")
targets_in_field = [int(el) for el in targets_in_field]
collected_points = 0
while True:
    commands = input()
    if commands == "Game over":
        print(game_over())
        break
    elif commands == "Reverse":
        targets_in_field = list(reverse_custom(targets_in_field))
        continue
    else:
        commands = commands.split("@")
        commands[1], commands[2] = int(commands[1]), int(commands[2])
        if commands[1] not in range(0, len(targets_in_field)):
            continue
    if commands[0] == "Shoot Left":
        collected_points, targets_in_field = shoot_left(commands[1], commands[2],
                                                        collected_points,
                                                        targets_in_field)
    elif commands[0] == "Shoot Right":
        collected_points, targets_in_field = shoot_right(commands[1], commands[2],
                                                         collected_points,
                                                         targets_in_field)
