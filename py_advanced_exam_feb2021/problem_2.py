from math import floor

size = int(input())
field = []
player_position = []
path = []
coins = 0
for row in range(size):
    field.append(input().split(" "))
    if "P" in field[row]:
        player_position.append(row)
        player_position.append(field[row].index("P"))

command = input()
def end_game(condition, coin):
    if condition:
        print(f"You won! You've collected {coin} coins.")
        print("Your path:")
        print(*path, sep="\n")
        exit(0)
        pass
    else:
        coin = floor(coin / 2)
        print(f"Game over! You've collected {coin} coins.")
        print("Your path:")
        if path:

            print(*path, sep="\n")
        exit(0)
    pass


def checking(r, c):
    if r not in range(size):
        end_game(False, coins)
    elif c not in range(size):
        end_game(False, coins)
    elif field[r][c] == "X":
        end_game(False, coins)
    else:
        return True


def up(r, c):
    r -= 1
    if checking(r, c):
        return [r, c]


def down(r, c):
    r += 1
    if checking(r, c):
        return [r, c]


def right(r, c):
    c += 1
    if checking(r, c):
        return [r, c]


def left(r, c):
    c -= 1
    if checking(r, c):
        return [r, c]


def action(r, c, coin):
    coin += int(field[r][c])
    # if int(field[r][c]) > 0:
    path.append([r, c])
    field[r][c] = 0

    return [r, c, coin]
    pass


while True:

    if command == "up":
        r_1, c_1 = up(player_position[0], player_position[1])
        player_position[0], player_position[1], coins = action(r_1, c_1, coins)
        if coins >= 100:
            end_game(True, coins)
    elif command == "down":
        r_1, c_1 = down(player_position[0], player_position[1])
        player_position[0], player_position[1], coins = action(r_1, c_1, coins)
        if coins >= 100:
            end_game(True, coins)
    elif command == "right":
        r_1, c_1 = right(player_position[0], player_position[1])
        player_position[0], player_position[1], coins = action(r_1, c_1, coins)
        if coins >= 100:
            end_game(True, coins)
    elif command == "left":
        r_1, c_1 = left(player_position[0], player_position[1])
        player_position[0], player_position[1], coins = action(r_1, c_1, coins)
        if coins >= 100:
            end_game(True, coins)
    command = input()