number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    hero = input().split(" ")
    name = hero[0]
    hit_points = float(hero[1])
    mana_points = float(hero[2])
    if hit_points > 100 or mana_points > 200:
        continue
    heroes.update({name: [hit_points, mana_points]})
command = input()

while not command == "End":
    command = command.split(" - ")
    action = command[0]

    if action == "CastSpell":
        name = command[1]
        mana_needed = float(command[2])
        spell_name = command[3]
        if heroes[name][1] < mana_needed:
            print(f"{name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[name][1] -= mana_needed
            print(f"{name} has successfully cast {spell_name} and now has {int(heroes[name][1])} MP!")

    elif action == "TakeDamage":
        name = command[1]
        damage = float(command[2])
        attacker = command[3]
        if heroes[name][0] - damage <= 0:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
        else:
            heroes[name][0] -= damage
            print(f"{name} was hit for {int(damage)} HP by {attacker} and now has {int(heroes[name][0])} HP left!")

    elif action == "Recharge":
        name = command[1]
        amount = float(command[2])
        if heroes[name][1] + amount > 200:
            print(f"{name} recharged for {int(200 - heroes[name][1])} MP!")
            heroes[name][1] = 200
        else:
            heroes[name][1] += amount
            print(f"{name} recharged for {int(amount)} MP!")

    elif action == "Heal":
        name = command[1]
        amount = float(command[2])
        if heroes[name][0] + amount > 100:
            print(f"{name} healed for {int(100 - heroes[name][0])} HP!")
            heroes[name][0] = 100
        else:
            heroes[name][0] += amount
            print(f"{name} healed for {int(amount)} HP!")
    command = input()

if not heroes == {}:
    heroes = {k: v for k, v in sorted(heroes.items(), key=lambda x: x)}
    heroes = {k: v for k, v in sorted(heroes.items(), key=lambda x: x[1][0], reverse=True)}
    for key, item in heroes.items():
        print(key)
        print(f"  HP: {int(item[0])}")
        print(f"  MP: {int(item[1])}")