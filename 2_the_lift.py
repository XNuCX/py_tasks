wag_places = 4
flag = False
people_waiting = int(input())
lift = input().split(" ")
lift_result = []
lift = [int(el) for el in lift]
for wag in lift:
    occup_places = wag
    while True:
        if occup_places < wag_places:
            if people_waiting == 0:
                if flag:
                    break
                print(f"The lift has empty spots!")
                flag = True
                break
            occup_places += 1
            people_waiting -= 1
        else:
            break
    if flag:
        lift_result.append(occup_places)
        continue
    lift_result.append(occup_places)
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(f"{' '.join([str(el) for el in lift_result])}")
elif flag:
    print(f"{' '.join([str(el) for el in lift_result])}")
elif not flag:
    print(f"{' '.join([str(el) for el in lift_result])}")






