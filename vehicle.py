class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner=None):
        if money >= self.price and self.owner is None:

            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
        if self.owner is not None:
            return f"Car already sold"
        elif money < self.price:
            return f"Sorry, not enough money"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type_1 = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type_1, model, price)
vehicle.sell()
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
vehicle.buy(45000, "Peter")
print(vehicle)
vehicle.sell()
vehicle.buy(45000, "Peter")
model_1 = "audi"
price_1 = 20000
vehicle_1 = Vehicle(vehicle_type_1, model_1, price_1)
vehicle_1.buy(36000, "George")
print(vehicle)
print(vehicle_1)




