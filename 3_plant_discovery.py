n = int(input())
plant_collection = {}
plant_wo_rating = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    plant_collection.update({plant: [int(rarity)]})

command = input()
while not command == "Exhibition":
    command = command.split(": ")
    action = command[0]
    if action == "Rate":
        plant, rating = command[1].split(" - ")
        if plant not in plant_collection:
            print("error")
        else:
            plant_collection[plant].append(int(rating))

    elif action == "Update":
        plant, new_rarity = command[1].split(" - ")
        if plant not in plant_collection:
            print("error")
        else:
            plant_collection[plant][0] = int(new_rarity)
    elif action == "Reset":
        plant = command[1]
        if plant not in plant_collection:
            print("error")
        else:
            del plant_collection[plant][1:]

    command = input()

print("Plants for the exhibition:")

plant_collection = {k: v for k, v in
                    sorted(plant_collection.items(),
                           key=lambda x: sum(x[1][1:]) / len(x[1][1:]) if x[1][1:] else 0.0, reverse=True)}
plant_collection = {k: v for k, v in sorted(plant_collection.items(), key=lambda x: x[1][0], reverse=True)}
for key, value in plant_collection.items():
    if value[1:]:
        print(f"- {key}; Rarity: {value[0]}; Rating: {(sum(value[1:])/len(value[1:])):.2f}")
    else:
        print(f"- {key}; Rarity: {value[0]}; Rating: 0.00")