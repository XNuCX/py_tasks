def func(col, it, val):
    shards_left = val - 250
    col[it] = shards_left
    name_obtained = it
    if name_obtained == "shards":
        name_obtained = "Shadowmourne"
    elif name_obtained == "fragments":
        name_obtained = "Valanyr"
    elif name_obtained == "motes":
        name_obtained = "Dragonwrath"
    result = f"{name_obtained} obtained!"
    col = {k_1: v_1 for k_1, v_1 in sorted(col.items(), key=lambda x: x)}
    result_1 = {k_2: v_2 for k_2, v_2 in sorted(col.items(), key=lambda x: x[1], reverse=True) if k_2 == "shards" or
                k_2 == "fragments" or k_2 == "motes"}
    result_2 = {k_3: v_3 for k_3, v_3 in col.items() if not (k_3 == "shards" or k_3 == "fragments" or k_3 == "motes")}
    return result, result_1, result_2


data = ""
collection = {"shards": 0, "motes": 0, "fragments": 0}
while True:
    data = input().split(" ")
    for index, el in enumerate(data):
        if (index+1) % 2 == 0:
            if el.lower() not in collection:
                collection.update({el.lower(): int(data[index-1])})
            else:
                collection[el.lower()] += int(data[index-1])
            for item, value in collection.items():
                if (item == "shards" or item == "motes" or item == "fragments") and int(value) >= 250:
                    r_1, r_2, r_3 = func(collection, item, int(value))
                    print(r_1)
                    for k, v in r_2.items():
                        print(f"{k}: {v}")
                    for k, v in r_3.items():
                        print(f"{k}: {v}")
                    exit()
