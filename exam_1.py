amount_of_experience_needed = float(input())
count_battles = int(input())
experience = 0.0
count = 0
flag = False
for i in range(count_battles):
    count += 1
    experience_input = float(input())
    if count % 3 == 0:
        experience += experience_input + experience_input * 0.15
        flag = True
    if count % 5 == 0:
        experience += experience_input - experience_input * 0.1
        flag = True
    if count % 15 == 0:
        experience += experience_input + experience_input * 0.05
        flag = True
    if not flag:
        experience += experience_input
    flag = False

    if experience >= amount_of_experience_needed:
        break

if experience < amount_of_experience_needed:
    needed_experience = amount_of_experience_needed - experience
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")
else:
    print(f"Player successfully collected his needed experience for {count} battles.")
