'''
Student ID: u3301989
Assignment: 1, Part5
Date Created: April 9, 2026
Last Updated: April 15, 2026
'''
#
#
# class Product:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description
#
#     def __str__(self):
#         return f"{self.name} - ${self.price}"
#
#
# class Inventory:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def get_products(self):
#         return self.products
#
#     def update_product(self, index, new_product):
#         if 0 <= index < len(self.products):
#             self.products[index] = new_product
#
#     def delete_product(self, index):
#         if 0 <= index < len(self.products):
#             self.products.pop(index)
#
#     def __str__(self):
#         return f"{self.products}"

class Product:
    def __init__(self):
        self.__name = ''
        self.__price = ''
        self.__description = ''

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f"{self.__name} {self.__price} {self.__description}"