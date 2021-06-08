from collections import deque
matrix = []
names = input().split(", ")
for _ in range(7):
    matrix.append(input().split(" "))

count = 0
turns = deque([{names[0]:0, "score": 501}, {names[1]:0, "score": 501}])

flag_end = False

def turn(turns_2):
    for key in turns_2[0].keys():
        turns_2[0][key] += 1
        return turns_2
while True:
    coordinates = input().replace("(", "").replace(")", "").split(", ")
    coordinates = [int(el) for el in coordinates]
    if coordinates[0] not in range(0, 7) or coordinates[1] not in range(0, 7) :
        turns = turn(turns)
        turns.append(turns.popleft())
        continue
    if matrix[coordinates[0]][coordinates[1]].isdigit():
        turns[0]["score"] -= int(matrix[coordinates[0]][coordinates[1]])
        turns = turn(turns)
    else:
        if matrix[coordinates[0]][coordinates[1]] == "D":
            sum_d = int(matrix[0][coordinates[1]]) + int(matrix[-1][coordinates[1]]) + \
                    int(matrix[coordinates[0]][0]) + int(matrix[coordinates[0]][-1])
            turns[0]["score"] -= sum_d  * 2
            turns = turn(turns)
        elif matrix[coordinates[0]][coordinates[1]] == "T":
            sum_t = int(matrix[0][coordinates[1]]) + int(matrix[-1][coordinates[1]]) + \
                    int(matrix[coordinates[0]][0]) + int(matrix[coordinates[0]][-1])
            turns[0]["score"] -= sum_t * 3
            turns = turn(turns)
        elif matrix[coordinates[0]][coordinates[1]] == "B":
            turns = turn(turns)
            flag_end = True
            break
    if turns[0]["score"] <= 0:
        # turns = turn(turns)
        flag_end = True
        break
    # for key in turns[0].keys():
    #     turns[0][key] += 1
    #     break

    turns.append(turns.popleft())

def get_name(data):
    for key, value in data.items():
        return key, value

if flag_end:
    name, count_turns = get_name(turns[0])
    print(f"{name} won the game with {count_turns} throws!")
else:
    pass
