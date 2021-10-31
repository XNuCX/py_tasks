from .food import Food
from .drink import Drink
from .product import Product
class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)
    def find(self, product_name: str):
        try:
            return [obj for obj in self.products if obj.name == product_name][0]
        except IndexError:
            return
    def remove(self, product_name):
            self.products = [obj for obj in self.products if not obj.name == product_name]
    def __repr__(self):
        products = "\n".join([f"{n.name}: {n.quantity}" for n in self.products])
        return products




