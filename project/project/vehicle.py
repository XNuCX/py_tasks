class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self._fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption):
        self._fuel_consumption = fuel_consumption

    def drive(self, kilometers):
        if self.fuel >= kilometers * self._fuel_consumption:
            self.fuel -= kilometers * self._fuel_consumption

