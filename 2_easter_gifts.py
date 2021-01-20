list_of_gifts = input().split(" ")
command = ""
index_gift = 0
act = ""
gift_name = ""
current_gift = ""
while True:
    command = input()
    if command == "No Money":
        break
    command = command.split(" ")
    act = command[0]
    gift_name = command[1]
    if len(command) == 3:
        index_gift = int(command[2])
    if act == "OutOfStock":
        for index, name in enumerate(list_of_gifts):
            if name == gift_name:
                list_of_gifts[index] = type(None)
            else:
                continue
    elif act == "Required":
        if index_gift in range(len(list_of_gifts)):
            list_of_gifts[index_gift] = gift_name
        else:
            continue

    elif act == "JustInCase":
        list_of_gifts[-1] = gift_name
list_of_gifts = [el for el in list_of_gifts if el is not type(None)]
print(f"{' '.join(list_of_gifts)}")

