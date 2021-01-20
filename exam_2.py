collection = input().split(" ")
# collection = [int(el) for el in collection]
count = 0
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" ")
    if command[0] == "reverse":
        start = int(command[2])
        stop = int(command[4])
        spot = collection[start:start+stop]
        spot.reverse()
        collection[start:start+stop] = spot

    if command[0] == "sort":
        start = int(command[2])
        stop = int(command[4])
        spot = collection[start:start + stop]
        spot.sort()
        collection[start:start + stop] = spot

    if command[0] == "remove":
        till = int(command[1])
        while not count == till:
            count += 1
            collection.pop(0)

collection = [str(el) for el in collection]
print(f"{', '.join(collection)}")
