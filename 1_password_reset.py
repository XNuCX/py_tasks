text = input()
commands = input()
new_pass = ""
substring = ""
while not commands == "Done":
    commands = commands.split(" ")
    action = commands[0]

    if action == "TakeOdd":
        for index in range(1, len(text), 2):
            new_pass += text[index]
        text = new_pass
        print(text)

    elif action == "Cut":
        index = int(commands[1])
        length = int((commands[2]))
        substring = text[index: index+ length]
        text = text.replace(substring, "", 1)
        print(text)

    elif action == "Substitute":
        substring = commands[1]
        substitute = commands[2]

        if substring in text:
            while substring in text:
                text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")

    commands = input()

print(f"Your password is: {text}")


