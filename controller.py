'''
Student ID: u3301989
Assignment: 1, Part5
Date Created: April 11, 2026
Last Updated: April 19, 2026
'''

from model import Product

class InventoryController:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, description):
        self.products.append(Product(name, price, description))

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