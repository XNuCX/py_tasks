concealed_message = input()
command = input()
temp_message = []
temp_message_1 = ""

while not command == "Reveal":
    command = command.split(":|:")
    instruction = command[0]

    if instruction == "InsertSpace":
        index = int(command[1])
        for char in concealed_message:
            temp_message.append(char)
        temp_message.insert(index, " ")
        for char in temp_message:
            temp_message_1 += str(char)
        concealed_message = temp_message_1[:]
        temp_message = []
        temp_message_1 = ""


        print(concealed_message)

    elif instruction == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            reversed_substring = substring[-1::-1]
            concealed_message = concealed_message.replace(substring, "", 1) + reversed_substring
            print(concealed_message)
        else:
            print("error")

    elif instruction == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")
