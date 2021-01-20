days_of_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())
water_supplay = float(input()) * count_of_players * days_of_adventure
food_supplay = float(input()) * count_of_players * days_of_adventure
day_energy = 0
count = 0
flag = False
while not days_of_adventure == 0:

    count += 1

    group_energy = group_energy - float(input())
    if count % 2 == 0:
        group_energy += group_energy * 0.05
        water_supplay -= water_supplay * 0.30
    if count % 3 == 0:
        food_supplay -= food_supplay / count_of_players
        group_energy += group_energy * 0.1
    days_of_adventure -= 1
    if group_energy <= 0:
        flag = True
        break

if not flag:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_supplay:.2f} food and {water_supplay:.2f} water.")
