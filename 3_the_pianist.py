n = int(input())
collection = {}
for _ in range(n):
    piece, composer, key = input().split("|")
    collection.update({piece: [composer, key]})
command = input()
while not command == "Stop":
    command = command.split("|")
    action = command[0]
    if action == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection.update({piece: [composer, key]})
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece in collection:
            print(f"Successfully removed {piece}!")
            del collection[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in collection:
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
if collection:
    collection = {k: v for k, v in sorted(collection.items(), key=lambda x: x[1][0])}
    collection = {k: v for k, v in sorted(collection.items(), key=lambda x: x)}
    for key, value in collection.items():
        print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")