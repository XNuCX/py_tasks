number_of_cars = int(input())
cars_colection = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars_colection.update({car: [float(mileage), float(fuel)]})

command = input()
while not command == "Stop":
    command = command.split(" : ")
    action = command[0]

    if action == "Drive":
        car = command[1]
        distance = float(command[2])
        fuel = float(command[3])
        if cars_colection[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_colection[car][0] += distance
            cars_colection[car][1] -= fuel
            print(f"{car} driven for {int(distance)} kilometers. {int(fuel)} liters of fuel consumed.")
            if cars_colection[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del cars_colection[car]

    elif action == "Refuel":
        car = command[1]
        fuel = float(command[2])
        if cars_colection[car][1] + fuel > 75:
            fuel = 75 - cars_colection[car][1]
            cars_colection[car][1] = 75.0
        else:
            cars_colection[car][1] += fuel

        print(f"{car} refueled with {int(fuel)} liters")

    elif action == "Revert":
        car = command[1]
        kilometers = float(command[2])

        if cars_colection[car][0] - kilometers <= 10000:
            cars_colection[car][0] = 10000.0
        else:
            cars_colection[car][0] -= kilometers
            print(f"{car} mileage decreased by {int(kilometers)} kilometers")

    command = input()

if cars_colection:
    cars_colection = {k: v for k, v in sorted(cars_colection.items(), key=lambda x: x)}
    cars_colection = {k: v for k, v in sorted(cars_colection.items(), key=lambda x: x[1][0], reverse=True)}

    for key, value in cars_colection.items():
        print(f"{key} -> Mileage: {int(value[0])} kms, Fuel in the tank: {int(value[1])} lt.")