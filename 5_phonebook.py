info = input()
phonebook = {}
while not info.isdigit():
    name, phone = info.split("-")
    phonebook[name] = phone
    info = input()
for _ in range(int(info)):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
