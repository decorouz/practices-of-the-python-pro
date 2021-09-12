# This clas contains method to add and remove a product by managing the data in this dictionary.

from collections import defaultdict
from product import Product


class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))

    def add_product(self, product, quantity=1):
        self.products[product.generate_sku()]["quantity"] += quantity

    def remove_product(self, product, quantity=1):
        sku = product.generate_sku()
        self.products[sku]["quantity"] -= quantity
        if self.products[sku]["quantity"] <= 0:
            del self.products[sku]

# shoe = Product("Shoes", "S", "yellow")


# blue_shoe = Product("Shoes", "M", "Blue")
# cart = ShoppingCart()
# cart.add_product(blue_shoe, 5)
# print(cart.products)

# cart.remove_product(blue_shoe, 4)
# print(cart.products)
# cart.add_product(shoe)
# cart.add_product(blue_shoe)
# cart.remove_product(shoe)
