names = input().split(", ")
coll = dict.fromkeys(names)
items = input()
while not items == "End":
    items = items.split("-")
    name = items[0]
    item = items[1]
    val = items[2]
    # if name in names:
    if name not in coll:
        coll[name] = {item: val}
    elif coll[name] is None:
        coll[name] = {item: val}
    elif item not in coll[name]:
        coll[name][item] = val
    # else:
    #     coll.update({name: {item: val}})
    items = input()


print('\n'.join([f"{key} -> Items: {len(value)}, Cost: {sum([int(v) for k, v in value.items()])}" for key, value in coll.items()]))
