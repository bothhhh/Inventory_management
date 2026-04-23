'''
Student ID: u3301989
Assignment: 1, Part5
Date Created: April 9, 2026
Last Updated: April 15, 2026
'''

# import model
#
#
# class InventoryController:
#     def __init__(self, inventory):
#         self.inventory = inventory
#
#     def create_product(self, name, price, description):
#         product = Product(name, price, description)
#         self.inventory.add_product(product)
#
#     def read_products(self):
#         return self.inventory.get_products()
#
#     def update_product(self, index, name, price, description):
#         new_product = Product(name, price, description)
#         self.inventory.update_product(index, new_product)
#
#     def delete_product(self, index):
#         self.inventory.delete_product(index)

from model5 import Product

class InventoryController:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, description):
        product = Product()
        product.set_name(name)
        product.set_price(price)
        product.set_description(description)
        self.products.append(product)

    def get_products(self):
        return self.products

    def get_product(self, index):
        return self.products[index]

    def update_product(self, index, name, price, description):
        if 0 <= index < len(self.products):
            self.products[index].set_name(name)
            self.products[index].set_price(price)
            self.products[index].set_description(description)

    def delete_product(self, index):
        if 0 <= index < len(self.products):
            del self.products[index]

    def __str__(self):
        return f"{self.products}"
