from .product import Product

class Drink(Product):

    def __init__(self, name, quantity=10):
        super(Drink, self).__init__(name, quantity)
