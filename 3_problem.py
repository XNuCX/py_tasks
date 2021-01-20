n = int(input())
collection = {}
command = input()
while not command == "Statistics":
    command = command.split("=")
    action = command[0]

    if action == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in collection:
            collection.update({username: [sent, received]})
        else:
            command = input()
            continue
    elif action == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in collection and receiver in collection:
            collection[sender][0] += 1
            if sum(collection[sender]) == n:
                print(f"{sender} reached the capacity!")
                del collection[sender]
            collection[receiver][1] += 1
            if sum(collection[receiver]) == n:
                print(f"{receiver} reached the capacity!")
                del collection[receiver]
    elif action == "Empty":
        username = command[1]
        if username == "All":
            collection = {}
        elif username in collection:
            del collection[username]

    command = input()

if not collection == {}:
    print(f"Users count: {len(collection)}")

    collection = {k: v for k, v in sorted(collection.items(), key=lambda x: x)}
    collection = {k: v for k, v in sorted(collection.items(), key=lambda x: x[1][1], reverse=True)}

    for key, value in collection.items():
        print(f"{key} - {sum(value)}")