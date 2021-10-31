from project.car import Car
class FamilyCar(Car):
    def __init__(self, fuel: float, horse_power: int):
        super(Car, self).__init__(fuel, horse_power)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.DEFAULT_FUEL_CONSUMPTION)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

