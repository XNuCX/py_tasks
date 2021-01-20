n = int(input())
command = ""
parking_data = {}
for i in range(n):
    command = input().split(" ")
    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username in parking_data:
            print(f"ERROR: already registered with plate number {parking_data[username]}")
        else:
            parking_data.update({username: plate})
            print(f"{username} registered {plate} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_data:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_data[username]
for k, v in parking_data.items():
    print(f"{k} => {v}")