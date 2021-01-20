activation_key = input()
command = input()
temp_key = None
while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        temp_key = []
        start = int(command[2])
        stop = int(command[3])
        if "Upper" in command:
            temp_key = [el for el in activation_key]
            for i in range(start, stop):
                temp_key[i] = str(temp_key[i]).upper()
            activation_key = "".join(temp_key)
            print(activation_key)
        elif "Lower" in command:
            temp_key = [el for el in activation_key]
            for i in range(start, stop):
                temp_key[i] = str(temp_key[i]).lower()
            activation_key = "".join(temp_key)
            print(activation_key)

    elif command[0] == "Slice":
        temp_key = ""
        start = int(command[1])
        stop = int(command[2])
        temp_key = activation_key[:start] + activation_key[stop:]
        activation_key = temp_key
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")