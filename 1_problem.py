username = input()
commands = input()

while not commands == "Sign up":
    commands = commands.split(" ")
    action = commands[0]

    if action == "Case":
        case = commands[1]
        if case == "lower":
            username = username.lower()
            print(f"{username}")
        elif case == "upper":
            username = username.upper()
            print(f"{username}")

    elif action == "Reverse":
        start = int(commands[1])
        stop = int(commands[2])
        if start in range(len(username)):
            if stop in range(len(username)):
                if start == 0:
                    substring = username[stop::-1]
                else:
                    substring = username[stop:start-1:-1]
                print(f"{substring}")
            else:
                commands = input()
                continue
        else:
            commands = input()
            continue

    elif action == "Cut":
        substring = commands[1]
        if substring in username:
            username = username.replace(substring, "")
            print(f"{username}")
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif action == "Replace":
        char = commands[1]
        if char in username:
            username = username.replace(char, "*")
        print(f"{username}")
    elif action == "Check":
        char = commands[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    commands = input()

