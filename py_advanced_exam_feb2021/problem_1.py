from collections import deque
fireworks_effects = deque([int(el) for el in input().split(", ")])
explosive_power = deque([int(el) for el in input().split(", ")])
created_effects = {}
effects = {"Palm": 0, "Willow": 0, "Crossette": 0}
flag = False
def check():
    if len(created_effects) == 3:
        if created_effects["Palm"] >= 3:
            if created_effects["Willow"] >= 3:
                if created_effects["Crossette"] >= 3:
                    return True
    return False
while fireworks_effects and explosive_power:

    if check():
        break
    effect = fireworks_effects.popleft()
    if effect <= 0:
        flag = True
        continue
    else:
        flag: False
    explosive = explosive_power.pop()
    if explosive <= 0:
        if not flag:
            fireworks_effects.appendleft(effect)
        continue

    if (effect + explosive) % 3 == 0 and (effect + explosive) % 5 != 0:
        if "Palm" in created_effects.keys():
            created_effects["Palm"] += 1
        else:
            created_effects["Palm"] = 1
        pass
    elif (effect + explosive) % 3 != 0 and (effect + explosive) % 5 == 0:
        if "Willow" in created_effects.keys():
            created_effects["Willow"] += 1
        else:
            created_effects["Willow"] = 1
        pass
    elif (effect + explosive) % 3 == 0 and (effect + explosive) % 5 == 0:
        if "Crossette" in created_effects.keys():
            created_effects["Crossette"] += 1
        else:
            created_effects["Crossette"] = 1
        pass
    else:
        effect -= 1

        fireworks_effects.append(effect)
        explosive_power.append(explosive)

if check():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in fireworks_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
if created_effects:
    for k, v in created_effects.items():
        effects[k] = v
for k, v in effects.items():
    print(f"{k} Fireworks: {v}")