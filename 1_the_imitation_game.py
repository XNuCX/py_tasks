message = input()
command = input()
while not command =="Decode":
    command = command.split("|")
    instruction = command[0]
    if instruction == "Move":
        num_letters = int(command[1])
        message = message[num_letters:] + message[:num_letters]
    elif instruction == "Insert":
        index = int(command[1])
        value = command[2]
        if index in range(len(message)):
            message = message[:index] + value + message[index:]
        else:
            message = message + value
    elif instruction == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {message}")