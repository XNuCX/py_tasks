import sys
status_of_myship = input().split(">")
status_of_myship = [int(el) for el in status_of_myship]
status_of_warship = input().split(">")
status_of_warship = [int(el) for el in status_of_warship]
max_health = int(input())
count = 0
flag = False
while True:
    command = input()
    if command == "Retire":
        status_of_myship = sum(status_of_myship)
        status_of_warship = sum(status_of_warship)
        print(f"Pirate ship status: {int(status_of_myship)}\nWarship status: {int(status_of_warship)}")
        break
    command = command.split(" ")
    act = command[0]
    if act == "Fire":
        index = int(command[1])
        if index not in range(len(status_of_warship)):
            continue
        damage = int(command[2])
        status_of_warship[index] -= damage
        if status_of_warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            sys.exit()
    if act == "Defend":
        start = int(command[1])
        stop = int(command[2])
        damage = int(command[3])
        for index, el in enumerate(status_of_myship):
            if index in range(start, stop + 1):
                status_of_myship[index] -= damage
                if status_of_myship[index] <= 0:
                    flag = True
        if flag:
            print("You lost! The pirate ship has sunken.")
            sys.exit()

    if act == "Repair":
        index = int(command[1])
        if index not in range(len(status_of_myship)):
            continue
        health = int(command[2])
        status_of_myship[index] += health
        if status_of_myship[index] > max_health:
            status_of_myship = max_health

    if act == "Status":
        status = [1 for el in status_of_myship if el < max_health * 0.2]
        count = sum(status)
        print(f"{count} sections need repair.")
