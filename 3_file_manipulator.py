import os

commands = input()
while not commands == "End":
    command, *rest = commands.split("-")
    if command == "Create":
        file_name = rest[0]
        print(file_name)
        with open(f"{file_name}", "w") as file_name:
            pass

    elif command == "Add":
        file_name = rest[0]
        content = rest[1]
        with open(file_name, "a") as file:
            file.writelines(f"{content}\n")
    elif command == "Replace":
        file_name = rest[0]
        old_string = rest[1]
        new_string = rest[2]
        try:
            file = open(file_name, "rt")
            data = file.read().replace(old_string, new_string)
            file.close()
            file = open(file_name, "wt")
            file.write(data)
            file.close()
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        file_name = rest[0]
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    commands = input()
