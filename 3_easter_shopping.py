list_of_shops = input().split(" ")
count_of_commands = int(input())
while count_of_commands > 0:
    count_of_commands -= 1
    command = input().split(" ")
    act = command[0]

    if act == "Include":
        shop = command[1]
        list_of_shops.append(shop)
    elif act == "Visit":
        which_shop = command[1]
        how_many = int(command[2])
        if 0 < how_many <= len(list_of_shops):
            if which_shop == "first":
                for i in range(how_many):
                    list_of_shops.pop(0)

            elif which_shop == "last":
                count = 0
                for index, el in reversed(list(enumerate(list_of_shops))):
                    if not count == how_many:
                        list_of_shops.pop(index)
                        count += 1
                    else:
                        break
            else:
                continue

    elif act == "Prefer":
        first_shop_i = int(command[1])
        second_shop_i = int(command[2])
        if first_shop_i in range(len(list_of_shops)) and second_shop_i in range(len(list_of_shops)):
            list_of_shops[first_shop_i], list_of_shops[second_shop_i] = list_of_shops[second_shop_i], \
                                                                        list_of_shops[first_shop_i]
        else:
            continue
    elif act == "Place":
        shop_name = command[1]
        resulted_index = int(command[2]) + 1
        if resulted_index in range(len(list_of_shops)):
            list_of_shops.insert(resulted_index, shop_name)
        else:
            continue

print(f"Shops left: \n{' '.join(list_of_shops)}")
