command = input()
city = {}
while not command == "Sail":
    command = command.split("||")
    town = command[0]
    people = int(command[1])
    gold = float(command[2])
    if town not in city:
        city.update({town: [people, gold]})
    else:
        city[town][0] += people
        city[town][1] += gold
    command = input()
while not command == "End":
    if command == "Sail":
        command = input()
        continue
    command = command.split("=>")
    event = command[0]
    if event == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = float(command[3])
        city[town][0] -= people
        if city[town][1] - gold < 0:
            gold = city[town][1]
            city[town][1] = 0
        else:
            city[town][1] -= gold
        print(f"{town} plundered! {int(gold)} gold stolen, {people} citizens killed.")
        if city[town][1] == 0 or city[town][0] == 0:
            del city[town]
            print(f"{town} has been wiped off the map!")

    elif event == "Prosper":
        town = command[1]
        gold = float(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            command = input()
            continue
        city[town][1] += gold
        print(f"{int(gold)} gold added to the city treasury. {town} now has {int(city[town][1])} gold.")

    command = input()

if not city == {}:
    city = {key: value for key, value in sorted(city.items(), key=lambda x: x)}
    city = {key: value for key, value in sorted(city.items(), key=lambda x: x[1][1], reverse=True)}
    print(f"Ahoy, Captain! There are {len(city)} wealthy settlements to go to:")
    for key, item in city.items():
        print(f"{key} -> Population: {item[0]} citizens, Gold: {int(item[1])} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")