text = input()
command = input()
while not command == "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        range_1 = range(len(text))
        if index in range_1:
            text = text[:index] + command[2] + text[index:]

        print(text)
    elif action == "Remove Stop":
        start = int(command[1])
        stop = int(command[2])
        range_1 = range(len(text))
        if start in range_1 and stop in range_1:
            text = text[:start] + text[stop+1:]

        print(text)
    elif action == "Switch":
        if command[1] in text:
            text = text.replace(command[1], command[2])

        print(text)

    command = str(input())

print(f"Ready for world tour! Planned stops: {text}")