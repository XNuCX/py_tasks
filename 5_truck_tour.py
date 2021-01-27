from collections import deque
pumps_num = int(input())
pumps_sequence = deque([])
tank = []
for i in range(pumps_num):
    pump = i
    petrol, distance = map(int, input().split())
    pumps_sequence.append({"petrol": petrol, "distance": distance})

count = 0
flag = False
while count < pumps_num:
    if flag:
        print(count)
        break
    for i in range(pumps_num):
        if pumps_sequence[i]["petrol"] + sum(tank) >= pumps_sequence[i]["distance"]:
            temp = pumps_sequence[i]["petrol"] - pumps_sequence[i]["distance"]
            tank.append(temp)
            if i == pumps_num -1:
                flag = True
        else:
            count += 1
            pumps_sequence.append(pumps_sequence.popleft())
            tank = []
            break